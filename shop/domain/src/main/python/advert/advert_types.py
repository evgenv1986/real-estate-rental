from abc import ABC, abstractmethod
from typing import Generic

from common.types.src.main.base.ValueObject import ValueObject, NegativeValueError
from common.types.src.main.common.Count import Count
from common.types.src.main.common.UID import UID, T
from common.types.src.main.error.BusinesError import BusinessError


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
    _value: Count
    def __init__(self, value: Count):
        self._value = value
        # super(FloorCount, self).__init__(value)
    @classmethod
    def create(cls, value: int)-> 'FloorCount':
        count = Count.create(value)
        # if not value.more_zero():
        #     raise FloorCountLessOrEqualZero()
        return FloorCount(count)

    # @classmethod
    # def create_from_str(cls, value: str):
    #     return FloorCount.create(Count.create(value))

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
    def next_id(self)-> 'AdvertID': pass

class FlatArea(ValueObject):
    _living_area: float
    _total_area: float
    def __init__(self,
                 living_area: Count,
                 total_area: Count) -> None:
        self._living_area = living_area
        self._total_area = total_area
    @classmethod
    def create (cls,
               living_area: float,
               total_area: float) -> 'FlatArea':
        if living_area <= 0 or living_area <= 0:
            raise NegativeValueError()
        return FlatArea(living_area, total_area)

    def living_area(self):
        return self._living_area


class Interior(ValueObject):
    _value: str
    def __init__(self, value: str):
        self._value = value
    @classmethod
    def create(cls, value: str) -> 'Interior':
        return Interior(value)
    def __eq__(self, obj: object) -> bool:
        if not isinstance(obj, Interior):
            return False
        other: Interior = obj
        return self._value == other._value


class Price(ValueObject):
    def __init__(self, value: float):
        self._value = value
    @classmethod
    def create(cls, value: float) -> 'Price':
        if value < 0:
            raise CreatePriceErrorNegativeValue()
        return Price(value)
    def __eq__(self, obj: object) -> bool:
        if not isinstance(obj, Price):
            return False
        other: Price = obj
        return self._value == other._value


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

class AdvertID(Generic[T], UID[int]):
    def __init__(self, _id: int):
        super().__init__(_id)


class AdvertAlreadyInWork(ABC):
    @abstractmethod
    def invoke(self, address: Address)-> bool:pass


class AdvertRejected(ABC):
    @abstractmethod
    def invoke(self, address: Address) -> bool: pass


class AdvertState:
    def next_state(self)-> 'AdvertState':
        pass
    def canChangeTo(self, param):
        pass

class AdvertWritedownedState(AdvertState):
    def next_state(self)-> 'AdvertState':
        return AdvertWritedownedState

class AdvertIdleState(AdvertState):
    def next_state(self)-> 'AdvertState':
        return AdvertWritedownedState()

    def canChangeTo(self, state: AdvertState)-> bool:
        if isinstance(self.next_state(), state.__class__):
            return True
        return False
        # return True \
        #     if AdvertWritedownedState == self.next_state() \
        #     else False
