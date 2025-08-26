from shop.domain.src.main.python.advert.advert import Advert, AlreadyInWorkAdvertError
from shop.domain.src.main.python.advert.advert_types import AdvertID, AdvertIdProvider, AdvertAlreadyInWork, \
    AdvertRejected
from shop.usecase.src.main.advert.TakeAdvertToWork import TakeAdvertToWork, AdvertData, AlreadyInWorkUseCaseError
from shop.usecase.src.main.advert.access.AdvertPersist import AdvertPersist




class TakeAdvertToWorkUseCase(TakeAdvertToWork):
    def __init__(
            self,
            advertIdProvider: AdvertIdProvider,
            advertAlreadyInWork: AdvertAlreadyInWork,
            advert_persist: AdvertPersist,
            advert_rejected: AdvertRejected
    ):
        self._advertIdProvider = advertIdProvider
        self._advertAlreadyInWork = advertAlreadyInWork
        self._advert_persist = advert_persist
        self._advert_rejected = advert_rejected
    def invoke(self, advert: 'AdvertData')-> AdvertID:
        try:
            advert = Advert.write_down(
                advert.contact,
                advert.address,
                advert.floor_count,
                advert.room_count,
                advert.area,
                advert.interior,
                advert.flat_floor,
                advert.price,
                advert.photos,
                advert.source_advert,
                self._advertIdProvider,
                self._advertAlreadyInWork,
                self._advert_rejected
            )
            self._advert_persist.save(advert)
            return advert.id()
        except AlreadyInWorkAdvertError as e:
            raise AlreadyInWorkUseCaseError()
