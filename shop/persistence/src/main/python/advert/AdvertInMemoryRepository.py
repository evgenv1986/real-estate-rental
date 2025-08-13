from shop.domain.src.main.python.advert.advert import Advert
from shop.usecase.src.main.advert.access.AdvertPersist import AdvertPersist


class AdvertPersistInMemoryRepository(AdvertPersist):
    def save(self, advert: Advert):
        pass