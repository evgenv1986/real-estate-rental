import unittest

from shop.domain.src.main.python.advert.advert import Advert
from shop.in_memory_persistence.InMemoryAdvertRepository import InMemoryAdvertRepository
from shop.domain.src.teatFixtures.Fixtures import advert_with_test_data

class InMemoryAdvertRepositoryTest(unittest.TestCase):
    def test_saving_advert_when_advert_does_not_exist(self):
        repository = InMemoryAdvertRepository()
        advert: Advert = advert_with_test_data()

        repository.save(advert)

        storedAdvert = repository.storage.get(advert.id)
        self.assertEqual(advert.id, storedAdvert.id)
