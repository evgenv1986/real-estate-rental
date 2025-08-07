from typing import TypeVar, Generic


T = TypeVar('T')

class UID(Generic[T]):
    _id = T
    def __init__(self, id: T):
        self._id = id
    def value(self) -> T:
        return self._id

class IntUID(UID[int]):
    def __init__(self, id: int) -> None:
        super().__init__(id)

    def value(self) -> int:
        return self._id