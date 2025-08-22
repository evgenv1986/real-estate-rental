import dataclasses

from common.types.src.main.base.DomainEntity import DomainEvent
from shop.domain.src.main.python.advert.advert_types import AdvertID

@dataclasses.dataclass
class AdvertWritedownedToWorkEvent(DomainEvent):
    def __init__(self, id: AdvertID):
        self._id = id