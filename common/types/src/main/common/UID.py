from typing import TypeVar, Generic

from common.types.src.main.base.ValueObject import ValueObject

T = TypeVar('T')

class UID(Generic[T], ValueObject):
    _id = T
    def __init__(self, _id: T):
        self._id = _id
    def value(self) -> T:
        return self._id

class IntUID(UID[int]):
    def __init__(self, _id: int) -> None:
        super().__init__(_id)

    def value(self) -> int:
        return self._id