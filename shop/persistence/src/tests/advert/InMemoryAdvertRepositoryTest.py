import unittest

from shop.domain.src.main.python.advert.advert import Advert
from shop.domain.src.teatFixtures.Fixtures import advert_with_test_data
from shop.in_memory_persistence.InMemoryAdvertRepository import TestPublisher, TestListener, InMemoryAdvertRepository


class InMemoryAdvertRepositoryTest(unittest.TestCase):
    def test_publish_event_AdvertWritedownedToWork_after_advert_writedown(self):
        publisher = TestPublisher()
        self.assertTrue(len (publisher.storage.items()) == 0)
        listener = TestListener()
        publisher.register(listener)
        # self.assertTrue(len(publisher.listeners) == 1)

        repository = InMemoryAdvertRepository(publisher)
        advert: Advert = advert_with_test_data()

        repository.save(advert)

        stored_advert = repository.storage.get(advert.id)
        self.assertEqual(advert.id, stored_advert.id)
        # self.assertTrue(len (publisher.storage.items()) == 1)


