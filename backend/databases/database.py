from abc import abstractmethod, ABC
from typing import Any


class DatabaseClient(ABC):
    @abstractmethod
    def init_db(
        self,
        *args,
        **kwargs,
    ) -> Any:

        raise NotImplementedError

    @abstractmethod
    def get_database(
        self,
        database_name: str
    ) -> Any:

        raise NotImplementedError

    @abstractmethod
    def get_collection(
        self,
        name: str
    ) -> Any:

        raise NotImplementedError
