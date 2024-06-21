from typing import List, Dict, Optional
from repositories.interfaces.IRepository import IRepository
from utils.Class import type_check, T

class InMemoryRepository(IRepository[T]):
    def __init__(self):
        self._data: Dict[int, T] = {}

    @type_check
    def add(self, entity: T) -> T:
        if entity.id in self._data:
            raise ValueError(f"Entity with id {entity.id} already exists.")
        if entity.id is None:
            entity.id = len(self._data.keys()) + 1

        self._data[entity.id] = entity
        
        return self._data[entity.id]

    @type_check
    def remove(self, entity: T) -> None:
        if entity.id not in self._data:
            raise ValueError(f"Entity with id {entity.id} does not exist.")
        del self._data[entity.id]

    @type_check
    def update(self, entity: T) -> T:
        if entity.id not in self._data:
            raise ValueError(f"Entity with id {entity.id} does not exist.")
        self._data[entity.id] = entity
        return self._data[entity.id]

    def get_by_id(self, id: int) -> Optional[T]:
        return self._data.get(id)

    def get_by_field(self, field: str, value: str) -> Optional[T]:
        for entity in self._data.values():
            if entity[field] == value:
                return entity
        return Null

    def list(self) -> List[T]:
        return list(self._data.values())
