from shop.domain.src.main.python.advert.advert import Advert
from shop.domain.src.main.python.advert.advert_types import AdvertID, AdvertIdProvider
from shop.usecase.src.main.advert.TakeAdvertToWork import TakeAdvertToWork, AdvertData


class TakeAdvertToWorkUseCase(TakeAdvertToWork):
    def __init__(self, advertIdProvider: AdvertIdProvider):
        self._advertIdProvider = advertIdProvider
    def invoke(self, advert: 'AdvertData')-> AdvertID:
        return Advert.create().id()
