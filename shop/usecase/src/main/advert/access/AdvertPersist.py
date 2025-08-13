from abc import ABC, abstractmethod

from shop.domain.src.main.python.advert.advert import Advert


class AdvertPersist(ABC):
    @abstractmethod
    def save(self, advert: Advert):pass