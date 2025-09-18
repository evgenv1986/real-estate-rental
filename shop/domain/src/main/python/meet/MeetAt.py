from dataclasses import dataclass
from datetime import datetime

from common.types.src.main.base.ValueObject import ValueObject


@dataclass
class MeetAt(ValueObject):
    value: datetime
    def __init__(self, meet_at: datetime):
        self.value = meet_at
