from abc import ABC, abstractmethod

from common.types.src.main.base.DomainEntity import DomainEvent


class Publisher(ABC):
    listeners: list [Listener] = []

    @abstractmethod
    def register(self, listener):pass

    @abstractmethod
    def publish(self, events: list[DomainEvent]):pass