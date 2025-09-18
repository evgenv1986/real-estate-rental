from abc import ABC
from shop.domain.src.main.python.meet.MeetID import MeetID

class MeetIdStore(ABC):
    def new_id(self) -> MeetID:pass
        # return MeetID(1)