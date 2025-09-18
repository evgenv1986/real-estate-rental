from dataclasses import dataclass

from common.types.src.main.base.ValueObject import ValueObject


@dataclass
class MeetID(ValueObject):
    def __init__(self, _id: int):
        self._id = _id

