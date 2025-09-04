from abc import ABC
from dataclasses import dataclass
from datetime import datetime
from typing import ClassVar, FrozenSet

from common.types.src.main.base.Either import Either
from shop.domain.src.main.python.advert.advert_types import AdvertID
from shop.domain.src.main.python.appointment.Appointment import Appointment


class MakeAppointment(ABC):
    def invoke(self, advert_id: AdvertID[int], meet_at: datetime)-> (
            Either['MakeAppointmentUseCaseError', Appointment]):
        pass

@dataclass
class MakeAppointmentUseCaseError:
    _allowed_subclasses: ClassVar[FrozenSet[str]] = frozenset({'AdvertNotFound', })
    def __init_subclass__(cls, **kwargs):
        if cls.__name__ not in MakeAppointmentUseCaseError._allowed_subclasses:
            raise TypeError(f"Cannot subclass {cls.__name__}. MakeAppointmentUseCaseError is sealed.")
        super().__init_subclass__(**kwargs)
    def message(self) -> str:pass

@dataclass
class AdvertNotFound(MakeAppointmentUseCaseError):
    def message(self) -> str:
        return f"Advert not found {self.message}"