import datetime

from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.types import ASGIApp

from log import log


class LoggingMiddleware(
    BaseHTTPMiddleware,
):
    def __init__(
        self,
        app: ASGIApp,
    ) -> None:

        super().__init__(
            app=app
        )
        self.log = log

    async def dispatch(
        self,
        request: Request,
        call_next,
    ) -> Response:

        formatted_request = {
            'method': request.method,
            'url': str(request.url),
            'host': request.headers.get('host'),
            # 'user-agent': request.headers.get('user-agent'),
            'query_params': request.query_params,
            # 'user': request.user,
            'path_params': request.path_params,
            'requested_at': str(datetime.datetime.now())
        }

        self.log.info(
            msg=formatted_request
        )

        response = await call_next(request)

        return response
