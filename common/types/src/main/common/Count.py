from abc import abstractmethod
from typing import Any, TypeVar, Generic

from common.types.src.main.base.ValueObject import ValueObject
from common.types.src.main.base.ValueObject import NegativeValueError

class Count(ValueObject):
    _value: int
    def __init__(self, value):
        self._value = value
    @classmethod
    def create(cls, value: int)-> 'Count':
        if value <= 0:
            raise NegativeValueError()
        return Count(value)
    def value(self)-> int:
        return self._value
    def more_zero(self):
        return self._value > 0

class CountError(Exception):pass
class StringAsIntError(Exception):pass
class StringNotANumberError(StringAsIntError):pass
class StringAsIntGetValueError(StringAsIntError):pass
class StringContainsNonNumericCharsError(CountError):
    def __init__(self):
        super().__init__(
            f"Не возможно создать строку которая содержит не цифровые символы.")
class CountAsFloatError(CountError):pass
