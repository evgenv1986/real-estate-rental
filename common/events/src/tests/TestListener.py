from typing import Generic, TypeVar

from common.types.src.main.base.DomainEntity import DomainEvent
from shop.domain.src.main.python.advert.advert_events import AdvertWritedownedToWorkEvent

T = TypeVar('T')

class TestListener(Generic[T]):
    event: DomainEvent
    def handle(self, event: DomainEvent):
        self.event = event
    def event_type(self):
        return AdvertWritedownedToWorkEvent
