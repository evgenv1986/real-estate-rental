from shop.domain.src.main.python.meet.MeetID import MeetID
from shop.domain.src.main.python.meet.MeetIdStore import MeetIdStore


class MeetIdStoreInMemory(MeetIdStore):
    def new_id(self) -> MeetID:
        return MeetID(1)