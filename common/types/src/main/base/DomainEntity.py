from abc import ABC
from typing import TypeVar, Generic

UID = TypeVar('UID')

class DomainEntity(ABC, Generic[UID]):
    _id: UID
    def __init__(self, id: UID):
            self._id = id
