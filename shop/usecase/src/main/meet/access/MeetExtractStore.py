import datetime

from shop.domain.src.main.python.advert.advert import Advert
from shop.domain.src.main.python.meet.Appointment import MeetAt


class MeetExtractStore:
    def meet_by_advert(self, advert: Advert)-> MeetAt:pass
