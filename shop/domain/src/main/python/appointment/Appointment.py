from dataclasses import dataclass
from datetime import datetime

from common.types.src.main.base.DomainEntity import DomainEntity
from shop.domain.src.main.python.advert.advert_types import AdvertID
from shop.domain.src.main.python.appointment.AppointmentEvents import AppointmentEvent, AppointmentID


@dataclass
class Appointment(DomainEntity):
    def meet_at(self)-> datetime:
        return self._meet_at

    def advert_id(self)-> AdvertID:
        return self._id

    @classmethod
    def make(cls, _id: AdvertID, meet_at: datetime) -> 'Appointment':
        appointment = Appointment(_id = _id, meet_at = meet_at)
        appointment_id = AppointmentID()
        event = AppointmentEvent(appointment_id)
        appointment.add_event(event)
        return appointment

    def __init__(self, _id: AdvertID, meet_at: datetime):
        super().__init__(_id)
        self._id = _id
        self._meet_at = meet_at

    def contains_event(self, finding):
        for event in self._events:
            if isinstance(event.__class__ == finding):
                return True
        return False