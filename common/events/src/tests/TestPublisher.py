from common.types.src.main.base.DomainEntity import DomainEvent
from common.events.src.tests.TestListener import TestListener


class TestPublisher:
    storage = {}
    listeners: list [TestListener] = []

    def register(self, listener):
        self.listeners.append(listener)

    def publish(self, events: list[DomainEvent]):
        for event in events:
            for listener in self.listeners_for(event):
                listener.handle(event)

    def listeners_for(self, event: DomainEvent)-> list[TestListener]:
        matched_listeners = []
        for listener in self.listeners:
            if isinstance(event, listener.event_type()):
                matched_listeners.append(listener)
        return matched_listeners
