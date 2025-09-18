from abc import ABC
from dataclasses import dataclass
from typing import ClassVar, FrozenSet

from common.types.src.main.base.Either import Either
from shop.domain.src.main.python.advert.advert_types import AdvertID
from shop.domain.src.main.python.meet.Meet import Meet
from shop.domain.src.main.python.meet.MeetAt import MeetAt


class MakeMeet(ABC):
    def invoke(self,
               advert_id: AdvertID[int],
               meet_at: MeetAt,)\
            -> (Either['MakeMeetUseCaseError', Meet]):
        pass

@dataclass
class MakeMeetUseCaseError:
    _adver_not_found = 'MakeAppointmentUseCaseError'
    _allowed_subclasses: ClassVar[FrozenSet[str]] = frozenset({'AdvertNotFound', })
    def __init_subclass__(cls, **kwargs):
        if cls.__name__ not in MakeMeetUseCaseError._allowed_subclasses:
            raise TypeError(f"Cannot subclass {cls.__name__}. MakeAppointmentUseCaseError is sealed.")
        super().__init_subclass__(**kwargs)
    def message(self) -> str:pass

    @property
    def adver_not_found(self):
        return self._adver_not_found


@dataclass
class AdvertNotFound(MakeMeetUseCaseError):
    def message(self) -> str:
        return f"Advert not found {self.message}"