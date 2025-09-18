from common.events.src.main.DomainEventListener import DomainEventListener
from common.events.src.main.DomainEventPublisher import DomainEventPublisher
from common.types.src.main.base.DomainEntity import DomainEvent


class WaitingMessageObjects(DomainEventPublisher):
    storage = {}
    listeners: list[DomainEventListener] = []

    def register(self, listener):
        self.listeners.append(listener)

    def send(self, events: list[DomainEvent]):
        for event in events:
            for listener in self.listeners_for(event):
                listener.handle(event)

    def listeners_for(self, event: DomainEvent) -> list[DomainEventListener]:
        matched_listeners = []
        for listener in self.listeners:
            if isinstance(event, listener.event_type()):
                matched_listeners.append(listener)
        return matched_listeners
