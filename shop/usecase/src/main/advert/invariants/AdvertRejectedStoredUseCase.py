from common.types.src.main.base.Either import Either
from shop.domain.src.main.python.advert.advert_types import AdvertRejected, Address
from shop.usecase.src.main.advert.access.ExtractedAdvert import ExtractedAdvert


class AdvertRejectedStoredUseCase(AdvertRejected):
    def __init(self, storageAdvert: ExtractedAdvert):
        self._storageAdvert = storageAdvert
    def invoke (self, address: Address):
        advert: Either = self._storageAdvert.by_address(address)
        if advert.is_right() and advert.value()._rejected:
            return True
        return False