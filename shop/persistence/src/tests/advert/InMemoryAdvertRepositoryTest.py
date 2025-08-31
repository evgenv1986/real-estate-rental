import unittest
from typing import Type

from common.types.src.main.base.DomainEntity import DomainEvent
from shop.domain.src.main.python.advert.advert import Advert
from shop.domain.src.main.python.advert.advert_events import AdvertWritedownedToWorkEvent
from shop.domain.src.main.python.advert.advert_types import AdvertID
from shop.domain.src.teatFixtures.Fixtures import advert_with_test_data
from shop.in_memory_persistence.InMemoryAdvertRepository import InMemoryAdvertRepository
from common.events.src.tests.TestListener import TestListener
from common.events.src.tests.TestPublisher import TestPublisher


class AnotherEvent(DomainEvent):
    pass


class InMemoryAdvertRepositoryTest(unittest.TestCase):
    def test_publish_event_AdvertWritedownedToWork_after_advert_writedown(self):
        publisher = TestPublisher()
        self.assertTrue(len (publisher.storage.items()) == 0)
        listener = TestListener()
        publisher.register(listener)

        repository = InMemoryAdvertRepository(publisher)
        advert: Advert = advert_with_test_data()

        repository.save(advert)

        stored_advert = repository.adverts.get(advert.id())
        self.assertEqual(advert.id, stored_advert.id)
        self.assertEqual(listener.event._id.value(), advert.id().value() )

    def test_publish_another_event(self):
        publisher = TestPublisher()
        listener = TestListener[AdvertWritedownedToWorkEvent]()
        publisher.register(listener)
        publisher.publish([AnotherEvent()])

    def test_contains_event_type(self):
        self.assertTrue(
            isinstance(
                AdvertWritedownedToWorkEvent(AdvertID(1)),
                TestListener().event_type())
        )