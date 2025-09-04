from dataclasses import dataclass

from common.types.src.main.base.DomainEntity import DomainEvent
from shop.domain.src.main.python.advert.advert_types import AdvertID


class AppointmentID:
    pass


@dataclass
class AppointmentEvent(DomainEvent):
    def __init__(self, appointment_id: AppointmentID):
        pass