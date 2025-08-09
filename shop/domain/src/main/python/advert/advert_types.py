from abc import ABC, abstractmethod

from common.types.src.main.base.ValueObject import ValueObject
from common.types.src.main.common.Count import IntCount, CountAsString, Count, CountAsFloat
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


class FloorCount(ValueObject):
    _value: IntCount
    def __init__(self, value: IntCount):
        self._value = value
        # super(FloorCount, self).__init__(value)
    @classmethod
    def create(cls, value: IntCount):
        if not value.more_zero():
            raise FloorCountLessOrEqualZero()
        return FloorCount(value)

    @classmethod
    def create_from_str(cls, value: str):
        return FloorCount.create(CountAsString.create(value))

    def more_zero(self):
        return self.more_zero() > 0
    def value(self):
        return self._value.value()

class FloorCountException(Exception):
    def __init__(self, message: str):
        super(FloorCountException, self).__init__(message)

class FloorCountLessOrEqualZero(FloorCountException):
    _message: str = f"Этаж не может быть меньше либо равен нолю"
    def __init__(self):
        super().__init__(self._message)


class RoomCount(ValueObject):
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
    def value(self):
        return self._value.value()

class RoomCountLessOrEqualZero(BusinessError):
    def __init__(self):
        self._message = "Количество комнат не может быть меньше либо равно нулю"
        # super().__init__('Количество комнат не может быть меньше либо равно нулю')


class AdvertIdProvider(ABC):
    @abstractmethod
    def next_id(self)-> UID: pass

class FlatArea(ValueObject):
    _living_area: Count
    _total_area: Count
    def __init__(self,
                 living_area: Count,
                 total_area: Count) -> None:
        self._living_area = living_area
        self._total_area = total_area
    @classmethod
    def create (cls,
               living_area: float,
               total_area: float) -> 'FlatArea':
        return FlatArea(
            CountAsFloat(living_area),
            CountAsFloat(total_area))

    def living_area(self):
        return self._living_area


class Interior(ValueObject):
    _value: str
    def __init__(self, value: str):
        self._value = value
    @classmethod
    def create(cls, value: str) -> 'Interior':
        return Interior(value)



class Price(ValueObject):
    def __init__(self, value: float):
        self._value = value
    @classmethod
    def create(cls, value: float) -> 'Price':
        if value < 0:
            raise CreatePriceErrorNegativeValue()
        return Price(value)


class CreatePriceErrorNegativeValue(BusinessError):
    pass


class Photo(ValueObject):
    def __init__(self, file: str):
        self._file = file
    @classmethod
    def create(cls, file: str) -> 'Photo':
        return Photo(file)

class Photos(ValueObject):
    def __init__(self, photos: list[Photo]):
        self._photos = photos
    @classmethod
    def create(cls, photos: list[Photo]) -> 'Photos':
        return Photos(photos)


class SourceAdvert:
    def __init__(self, source: str):
        self._source = source
    @classmethod
    def create(cls, source: str) -> 'SourceAdvert':
        return SourceAdvert(source)
    def __eq__(self, obj: object) -> bool:
        if not isinstance(obj, SourceAdvert):
            return False
        other: SourceAdvert = obj
        return other._source == self._source

