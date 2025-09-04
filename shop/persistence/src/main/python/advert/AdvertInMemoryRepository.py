from shop.domain.src.main.python.advert.advert import Advert
from shop.usecase.src.main.advert.access.AdvertPersist import AdvertPersist


class AdvertPersistInMemoryRepository_for_delete(AdvertPersist):
    def save(self, advert: Advert):
        pass