from abc import ABC, abstractmethod
from typing import TypeVar, Generic

from common.types.src.main.base.DomainEntity import DomainEvent

T = TypeVar('T')

class Listener(ABC, Generic[T]):
    @abstractmethod
    def handle(self, event: DomainEvent):pass
