from datetime import datetime

from common.types.src.main.base.Either import Either, Left, Right
from shop.domain.src.main.python.advert.advert import Advert
from shop.domain.src.main.python.advert.advert_types import AdvertID
from shop.usecase.src.main.advert.MakeAppointment import MakeAppointment, AdvertNotFound, MakeAppointmentUseCaseError
from shop.domain.src.main.python.appointment.Appointment import Appointment
from shop.usecase.src.main.advert.access.ExtractedAdvert import ExtractedAdvert


class MakeAppointmentUseCase(MakeAppointment):
    def __init__(self,
                 advert_id: AdvertID[int],
                 extracted_advert: ExtractedAdvert):
        self._extractedAdvert = extracted_advert

    def invoke(self, advert_id: AdvertID[int], meet_at: datetime) -> Either[MakeAppointmentUseCaseError, Appointment]:
        if self._extractedAdvert.advert_by_id(advert_id).is_left():
            return Left(AdvertNotFound())
        else:
            return Right(Appointment.make(
                    self._extractedAdvert.advert_by_id(advert_id).value.id(),
                    meet_at))
