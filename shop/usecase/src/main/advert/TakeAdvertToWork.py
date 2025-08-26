from abc import ABC
from typing import NamedTuple, ClassVar, FrozenSet

from common.types.src.main.error.BusinesError import BusinessError
from shop.domain.src.main.python.advert.advert_types \
    import (Address, FloorCount, RoomCount, \
            FlatArea, Interior, Count, Price, \
            Photos, SourceAdvert,
            AdvertID)
from shop.domain.src.main.python.advert.Contact import Contact


class TakeAdvertToWork(ABC):
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

class TakeAdvertInWorkUseCaseError(BusinessError):
    _allowed_subclasses: ClassVar[FrozenSet[str]] = frozenset({'AlreadyInWorkUseCaseError',})
    def __init_subclass__(cls, **kwargs):
        if cls.__name__ not in TakeAdvertInWorkUseCaseError._allowed_subclasses:
            raise TypeError(f"Cannot subclass {cls.__name__}. Contact is sealed.")
        super().__init_subclass__(**kwargs)

class AlreadyInWorkUseCaseError(TakeAdvertInWorkUseCaseError):
    def message(self):
        return "Объявление уже находится в работе"
