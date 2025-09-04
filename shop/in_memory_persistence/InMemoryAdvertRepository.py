from typing import Dict, ClassVar, FrozenSet

from common.events.src.tests.TestPublisher import TestPublisher
from common.types.src.main.base.Either import Either, Right, Left
from common.types.src.main.error.BusinesError import BusinessError
from shop.domain.src.main.python.advert.advert import Advert
from shop.domain.src.main.python.advert.advert_types import AdvertID, Address
from shop.usecase.src.main.advert.access.AdvertPersist import AdvertPersist
from shop.usecase.src.main.advert.access.ExtractedAdvert import ExtractedAdvert



class InMemoryAdvertRepository(AdvertPersist, ExtractedAdvert):
    adverts: Dict[AdvertID, Advert] = {}
    def __init__(self, publisher: TestPublisher):
        self.adverts: Dict[AdvertID, Advert] = {}
        self.publisher = publisher
    def save(self, advert: Advert) -> None:
        self.publisher.publish(advert.pop_events())
        self.adverts[advert.id()] = advert

    def by_address(self, address: Address) -> Either['AdvertRepositoryError', Advert]:
        for _id, ad in self.adverts.items():
            if ad._address == address:
                return Right (ad)
            break
        return Left(NotFoundAdvertError())

    def advert_by_id(self, _id: AdvertID)-> Either['AdvertRepositoryError', Advert]:
        if self.adverts.get(_id).id().value() == _id.value():
            return Right(self.adverts.get(_id))
        else:
            return Left(NotFoundAdvertError())




class AdvertRepositoryError(BusinessError):
    _allowed_subclasses: ClassVar[FrozenSet[str]] = frozenset({'NotFoundAdvertError', })

    def __init_subclass__(cls, **kwargs):
        if cls.__name__ not in AdvertRepositoryError._allowed_subclasses:
            raise TypeError(f"Cannot subclass {cls.__name__}. Contact is sealed.")
        super().__init_subclass__(**kwargs)

class NotFoundAdvertError(AdvertRepositoryError):
    def __init__(self):
        super().__init__()
    def message(self) -> str:
        return f"Advert not found"