from abc import ABC
from dataclasses import dataclass
from datetime import datetime

from common.types.src.main.base.AggregateRoot import AggregateRoot
from common.types.src.main.base.Either import Either, Left, Right
from common.types.src.main.error.BusinesError import BusinessError
from shop.domain.src.main.python.advert.advert import Advert
from shop.domain.src.main.python.advert.advert_types import AdvertID
from shop.domain.src.main.python.meet.MeetEvents import MeetMakedEvent
from shop.domain.src.main.python.meet.MeetAt import MeetAt
from shop.domain.src.main.python.meet.MeetID import MeetID
from shop.domain.src.main.python.meet.MeetIdStore import MeetIdStore
from shop.domain.src.main.python.meet.MeetingTimeNotYetComeCondition import MeetingTimeNotYetComeCondition

class Meet(AggregateRoot):
    def meet_at(self)-> MeetAt:
        return self._meet_at

    def advert_id(self)-> AdvertID:
        return self._advert_id

    @classmethod
    def make(cls,
             advert: Advert,
             meet_at: MeetAt,
             meet_id_store: MeetIdStore,
             meet_in_future: MeetingTimeNotYetComeCondition,
             ) -> Either['MeetCanNotBeInLastTime', 'Meet']:
        if not meet_in_future.invoke(meet_at):
            return Left(MeetCanNotBeInLastTime())
        else:
            meet_id = meet_id_store.new_id()
            meet = Meet(
                _id = meet_id,
                meet_at = meet_at,
                advert_id = advert.id())
            event = MeetMakedEvent(meet_id)
            meet.add_event(event)
            return Right(meet)

    def __init__(self,
                 _id: MeetID,
                 meet_at: MeetAt,
                 advert_id: AdvertID):
        super().__init__(_id)
        self._id = _id
        self._meet_at = meet_at
        self._advert_id = advert_id

    def contains_event(self, finding):
        for event in self._events:
            if isinstance(event, finding):
                return True
        return False

    def id(self):
        return self._id


class MeetCanNotBeInLastTime(BusinessError, ABC):pass