from abc import ABC
from typing import NamedTuple

from shop.domain.src.main.python.advert.advert_types \
    import (Address, FloorCount, RoomCount, \
            FlatArea, Interior, Count, Price, \
            Photos, SourceAdvert,
            AdvertID)
from shop.domain.src.main.python.advert.Contact import Contact


class TakeAdvertInWork(ABC):
    def invoke(self, advert: 'AdvertData')-> AdvertID:
        pass


class AdvertData(NamedTuple):
    contact: Contact
    address: Address
    floor_count: FloorCount
    room_count: RoomCount
    area: FlatArea
    interior: Interior
    flat_floor: Count
    price: Price
    photos: Photos
    source_advert: SourceAdvert
    # advert_id_provider: AdvertIdProvider

class TakeAdvertInWorkUseCaseError:pass
class AlreadyInWorkUseCaseError(TakeAdvertInWorkUseCaseError):pass