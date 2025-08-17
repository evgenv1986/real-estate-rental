from abc import ABC
from typing import Dict

from shop.domain.src.main.python.advert.advert import Advert
from shop.domain.src.main.python.advert.advert_types import Address, AdvertID


class ExtractedAdvert(ABC):
    id = [Address]
    advert = [Advert]
    adverts: Dict[AdvertID, Advert] = {}

    def __init__(self):
        self.adverts: Dict[AdvertID, Advert] = {}
    def by_address(self, address: Address) -> Advert:
        for id, ad in self.adverts.items():
            if ad.address == address:
                return ad
            break
        raise Exception(f"No advert with address {address}")
