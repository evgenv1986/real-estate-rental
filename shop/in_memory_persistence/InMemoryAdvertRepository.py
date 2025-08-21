from shop.domain.src.main.python.advert.advert import Advert
from shop.usecase.src.main.advert.access.AdvertPersist import AdvertPersist


class InMemoryAdvertRepository(AdvertPersist):
    def __init__(self):
        self.storage = {}

    def save(self, advert: Advert) -> Advert:
        self.storage[advert.id] = advert

