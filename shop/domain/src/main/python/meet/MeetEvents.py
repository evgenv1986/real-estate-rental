from dataclasses import dataclass
from common.types.src.main.base.DomainEntity import DomainEvent
from shop.domain.src.main.python.meet.MeetID import MeetID


@dataclass
class MeetMakedEvent(DomainEvent):
    def __init__(self, appointment_id: MeetID):
        super().__init__()
        self._id = appointment_id