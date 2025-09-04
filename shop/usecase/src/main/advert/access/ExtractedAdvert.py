from abc import ABC, abstractmethod

from common.types.src.main.base.Either import Either
from common.types.src.main.error.BusinesError import BusinessError
from shop.domain.src.main.python.advert.advert import Advert
from shop.domain.src.main.python.advert.advert_types import Address, AdvertID


class ExtractedAdvert(ABC):
    @abstractmethod
    def by_address(self, address: Address) -> Either:pass
    @abstractmethod
    def advert_by_id(self, _id: AdvertID)-> Either['ExtractedAdvertError', Advert]:
        pass

class ExtractedAdvertError(BusinessError):pass