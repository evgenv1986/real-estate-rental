from abc import ABC
from typing import OrderedDict

from common.types.src.main.common.UID import UID
from shop.domain.src.main.python.advert.advert import Advert
from shop.domain.src.main.python.advert.advert_types import Address


class ExtractedAdvert(ABC):
    id = [Address]
    advert = [Advert]
    adverts: dict(zip(id, advert))

    def by_address(self, address: Address) -> Advert:
        for id, ad in self.advert.items():
            if ad.address == address:
                return ad
            break
        raise Exception(f"No advert with address {address}")

