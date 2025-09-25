from datetime import datetime

from common.types.src.main.common.UID import UID
from shop.domain.src.main.python.advert.advert_types import AdvertID
from shop.domain.src.main.python.meet.MeetAt import MeetAt
from shop.domain.src.main.python.meet.MeetID import MeetID
from shop.usecase.src.main.meet.MakeMeet import MakeMeet

class MakeMeetEndPoint:
    def __init__(self, make_meet: MakeMeet):
        self.make_meet = make_meet
    def execute(self, id: int, meet_at: datetime):
        meet_id: MeetID = (self.make_meet
                .invoke(AdvertID(id), MeetAt(meet_at))
                .value.id())
        return meet_id._id