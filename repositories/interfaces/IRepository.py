from abc import ABC, abstractmethod
from typing import List, TypeVar, Generic
from utils.Class import T

class IRepository(ABC, Generic[T]):
    @abstractmethod
    def add(self, entity: T) -> T:
        raise NotImplementedError

    @abstractmethod
    def remove(self, entity: T) -> None:
        raise NotImplementedError

    @abstractmethod
    def update(self, entity: T) -> T:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, id: int) -> T:
        raise NotImplementedError

    @abstractmethod
    def get_by_field(self, field: str, value: str) -> T:
        raise NotImplementedError

    @abstractmethod
    def list(self) -> List[T]:
        raise NotImplementedError

    @classmethod
    def _type(cls):
        raise NotImplementedError("Subclasses should implement this method to specify the type.")
