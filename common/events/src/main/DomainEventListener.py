from abc import ABC, abstractmethod
from typing import TypeVar, Generic

from common.types.src.main.base.DomainEntity import DomainEvent
from shop.domain.src.main.python.advert.advert_events import AdvertWritedownedToWorkEvent
from shop.domain.src.main.python.meet.MeetEvents import MeetMakedEvent

T = TypeVar('T')

class DomainEventListener(ABC, Generic[T]):
    @abstractmethod
    def handle(self, event: DomainEvent):pass
    @abstractmethod
    def event_type(self):pass


class TestListener(DomainEventListener, Generic[T]):
    event: DomainEvent
    def handle(self, event: DomainEvent):
        self.event = event
    def event_type(self):
        return AdvertWritedownedToWorkEvent

class SMSMeetMakedRule(DomainEventListener, Generic[T]):
    event: DomainEvent
    def handle(self, event: DomainEvent):
        self.event = event
    def event_type(self):
        return MeetMakedEvent
