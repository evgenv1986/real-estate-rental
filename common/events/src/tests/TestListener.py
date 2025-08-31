from typing import Generic, TypeVar

from shop.domain.src.main.python.advert.advert_events import AdvertWritedownedToWorkEvent

T = TypeVar('T')

class TestListener(Generic[T]):
    event: AdvertWritedownedToWorkEvent
    def handle(self, event: AdvertWritedownedToWorkEvent):
        self.event = event
    def event_type(self):
        return AdvertWritedownedToWorkEvent
