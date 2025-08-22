from common.types.src.main.base.DomainEntity import DomainEvent
from shop.domain.src.main.python.advert.advert import Advert
from shop.usecase.src.main.advert.access.AdvertPersist import AdvertPersist



class TestPublisher:
    storage = {}
    listeners = []

    def register(self, listener):
        self.listeners.append(listener)

    def publish(self, events: list[DomainEvent]):
        pass


class TestListener:
    def handle(self, event: DomainEvent):
        self.event = event

class InMemoryAdvertRepository(AdvertPersist):
    def __init__(self, publisher: TestPublisher):
        self.storage = {}
        self.publisher = publisher
    def save(self, advert: Advert) -> None:
        self.publisher.publish(advert.pop_events())
        self.storage[advert.id] = advert
