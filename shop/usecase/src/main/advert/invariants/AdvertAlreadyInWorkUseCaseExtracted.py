from shop.domain.src.main.python.advert.advert import Advert
from shop.domain.src.main.python.advert.advert_types import AdvertAlreadyInWork, AdvertIdProvider, Address
from shop.usecase.src.main.advert.access.ExtractedAdvert import ExtractedAdvert


class AdvertAlreadyInWorkUseCaseExtracted(AdvertAlreadyInWork):
    def __init__(self, extracted_advert: ExtractedAdvert):
        self.extracted_advert = extracted_advert
    def invoke(self, address: Address) -> bool:
        return True
        advert: Either = self.extracted_advert.by_address(address)
        return True if advert else False