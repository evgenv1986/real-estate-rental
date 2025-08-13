from sqlite3 import IntegrityError

from shop.domain.src.main.python.advert.advert import Advert, AlreadyInWorkAdvertError
from shop.domain.src.main.python.advert.advert_types import AdvertID, AdvertIdProvider, AdvertAlreadyInWork
from shop.usecase.src.main.advert.TakeAdvertInWork import TakeAdvertInWork, AdvertData, AlreadyInWorkUseCaseError


class AdvertPersist:
    pass


class TakeAdvertToWorkUseCase(TakeAdvertInWork):
    def __init__(
            self,
            advertIdProvider: AdvertIdProvider,
            advertAlreadyInWork: AdvertAlreadyInWork,
            advert_persist: AdvertPersist
    ):
        self._advertIdProvider = advertIdProvider
        self._advertAlreadyInWork = advertAlreadyInWork
        self._advert_persist = advert_persist
    def invoke(self, advert: 'AdvertData')-> AdvertID:
        try:
            advert = Advert.create(
                advert.contact,
                advert.address,
                advert.address.street,
                advert.floor_count,
                advert.room_count,
                advert.area,
                advert.interior,
                advert.flat_floor,
                advert.price,
                advert.photos,
                advert.source_advert,
                self._advertIdProvider,
                self._advertAlreadyInWork
            )
            self._advert_persist.save(advert)
            return advert.id()
        except AlreadyInWorkAdvertError as e:
            raise AlreadyInWorkUseCaseError()
