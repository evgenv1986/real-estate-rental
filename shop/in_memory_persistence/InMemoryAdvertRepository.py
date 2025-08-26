from typing import Generic, TypeVar, Dict

from common.types.src.main.base.DomainEntity import DomainEvent
from shop.domain.src.main.python.advert.advert import Advert
from shop.domain.src.main.python.advert.advert_events import AdvertWritedownedToWorkEvent
from shop.domain.src.main.python.advert.advert_types import AdvertID, Address
from shop.usecase.src.main.advert.access.AdvertPersist import AdvertPersist
from shop.usecase.src.main.advert.access.ExtractedAdvert import ExtractedAdvert

T = TypeVar('T')

class TestListener(Generic[T]):
    event: AdvertWritedownedToWorkEvent
    def handle(self, event: AdvertWritedownedToWorkEvent):
        self.event = event
    def event_type(self):
        return AdvertWritedownedToWorkEvent


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


class InMemoryAdvertRepository(AdvertPersist, ExtractedAdvert):
    adverts: Dict[AdvertID, Advert] = {}
    def __init__(self, publisher: TestPublisher):
        self.adverts: Dict[AdvertID, Advert] = {}
        self.publisher = publisher
    def save(self, advert: Advert) -> None:
        self.publisher.publish(advert.pop_events())
        self.adverts[advert.id()] = advert
    def by_address(self, address: Address) -> Advert:
        for id, ad in self.adverts.items():
            if ad._address == address:
                return ad
            break
        raise Exception(f"No advert with address {address}")