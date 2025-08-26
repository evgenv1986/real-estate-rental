from abc import ABC, abstractmethod

from shop.domain.src.main.python.advert.advert import Advert
from shop.domain.src.main.python.advert.advert_types import Address


class ExtractedAdvert(ABC):
    @abstractmethod
    def by_address(self, address: Address) -> Advert:pass