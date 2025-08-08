from abc import ABC, abstractmethod

from common.types.src.main.base.ValueObject import ValueObject
from common.types.src.main.common.Count import Count, StringAsInt
from common.types.src.main.common.UID import UID
from common.types.src.main.error.BusinesError import BusinessError


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
    def street(self):
        return self._street
    def house(self):
        return self._house


class FloorCount(Count):
    _value: Count
    def __init__(self, value: Count):
        self._value = value
        # super(FloorCount, self).__init__(value)
    @classmethod
    def create(cls, value: Count):
        if not value.more_zero():
            raise FloorCountLessOrEqualZero()
        return FloorCount(value)

    @classmethod
    def create_from_str(cls, value: str):
        return FloorCount.create(StringAsInt.create(value))

    def more_zero(self):
        return self.more_zero() > 0
    def value(self):
        return self._value.value()

class FloorCountException(Exception):
    # _message: str = f"Этаж не может быть меньше либо равен нолю"
    def __init__(self, message: str):
        super(FloorCountException, self).__init__(message)

class FloorCountLessOrEqualZero(FloorCountException):
    _message: str = f"Этаж не может быть меньше либо равен нолю"
    def __init__(self):
        super().__init__(self._message)


class RoomCount(Count):
    _value: Count
    def __init__(self, value: Count):
        # super().__init__(value)
        self._value = value

    @classmethod
    def create(cls, value: Count):
        if not value.more_zero():
            raise RoomCountLessOrEqualZero()
        return RoomCount(value)

    def more_zero(self):
        return self._value.more_zero()

class RoomCountLessOrEqualZero(BusinessError):
    def __init__(self):
        super().__init__(
            f"Количество комнат не может быть меньше либо равно нулю")


class AdverIdProvider(ABC):
    @abstractmethod
    def next_id(self)-> UID: pass
