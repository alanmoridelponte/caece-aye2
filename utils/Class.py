from typing import TypeVar
from functools import wraps

T = TypeVar('T')

def type_check(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        # Suponemos que la entidad es siempre el primer argumento después de self
        entity = args[0]
        if not isinstance(entity, self._type()):
            raise TypeError(f"Only {self._type().__name__} instances can be handled by the repository.")
        return func(self, *args, **kwargs)
    return wrapper