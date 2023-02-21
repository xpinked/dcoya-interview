import logging

from configurations.config import settings


class LogFormatter(
    logging.Formatter,
):
    def __init__(
        self,
    ) -> None:
        format = '%(asctime)s - %(filename)s - %(levelname)s - %(message)s'
        super().__init__(
            fmt=format,
        )


def setup_logger(
) -> logging.Logger:
    log_level = logging.getLevelName(
        level=settings.LOG_LEVEL,
    )

    log = logging.getLogger(
        name='backend',
    )

    log.setLevel(
        level=log_level,
    )

    formatter_extra = LogFormatter()
    log_stream_handler = logging.StreamHandler()

    log_stream_handler.setLevel(
        level=log_level,
    )

    log_stream_handler.setFormatter(
        fmt=formatter_extra,
    )

    log.addHandler(
        hdlr=log_stream_handler,
    )

    return log


log = setup_logger()
