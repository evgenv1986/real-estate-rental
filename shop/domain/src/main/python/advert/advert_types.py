from enum import Enum

from common.types.src.main.base.valueObject import ValueObject
from common.types.src.main.common.count import Count, StringAsInt


class Contact (ValueObject):
    _telephone: str
    def __init__(self, telephone: str):
        self._telephone = telephone
    def telephone(self):
        return self._telephone


class Address(ValueObject):
    _street: str
    _house: str
    def __init__(self, street, house):
        self._street = street
        self._house = house


class FloorCount(Count):
    def __init__(self, value: Count):
        self.value = value
    @classmethod
    def create(cls, value: Count):
        if not value.more_zero():
            raise FloorCountLessOrEqualZero()
        return FloorCount(value)

    @classmethod
    def createFromStr(cls, value: str):
        return FloorCount.create(StringAsInt.create(value))

    def more_zero(self):
        return self.more_zero() > 0

class FloorCountException(Exception):
    def __init__(self, message: str):pass

class FloorCountLessOrEqualZero(FloorCountException):
    _message: str = f"Этаж не может быть меньше либо равен нолю"
    def __init__(self):
        super().__init__(self._message)