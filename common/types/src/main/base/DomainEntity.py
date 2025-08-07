from abc import ABC

from common.types.src.main.common.UID import UID


class DomainEntity(ABC):
    _id: UID
    def __init__(self, id: UID):
            self._id = id
