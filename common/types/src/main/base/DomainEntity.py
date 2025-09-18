from random import random
from xmlrpc.client import DateTime

from common.types.src.main.common.UID import UID


class EventStoreID:
    def next(self):
        return UID[int](random())


class DomainEvent:
    _event_id: UID
    _created: DateTime
    def __init__(self):
        self._event_id = EventStoreID().next()
        self._created = DateTime()

class DomainEntity:
    _id: UID
    _events: list[DomainEvent]
    def __init__(self, _id: UID):
        self._id = _id
        self._events = []
    def add_event(self, event: DomainEvent):
        self._events.append(event)
    def pop_events(self):
        events = self._events.copy()
        self._events = []
        return events