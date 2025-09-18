from abc import ABC, abstractmethod

from common.events.src.main.DomainEventListener import DomainEventListener
from common.types.src.main.base.DomainEntity import DomainEvent


class DomainEventPublisher(ABC):
    listeners: list [DomainEventListener] = []
    @abstractmethod
    def register(self, listener):pass
    @abstractmethod
    def notify(self, events: list[DomainEvent]):pass

