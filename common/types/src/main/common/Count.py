from abc import abstractmethod

from common.types.src.main.base.ValueObject import ValueObject
from common.types.src.main.base.ValueObject import NegativeValueError

class Count(ValueObject):
    @abstractmethod
    def value(self)-> int:
        pass
    @abstractmethod
    def more_zero(self):
        pass
    @abstractmethod
    def __eq__(self, obj: object) -> bool:pass


class IntCount(Count):
    _value: int
    def __init__(self, value):
        self._value = value
    @classmethod
    def create(cls, value: int)-> 'IntCount':
        if value < 0:
            raise NegativeValueError()
        return IntCount(value)
    def value(self)-> int:
        return self._value
    def more_zero(self):
        return self._value > 0
    def __eq__(self, obj: object) -> bool:
        pass


class CountAsString(Count):
    _value: str
    def __init__(self, value):
        self._value = value
    @classmethod
    def create(cls, value: str):
        if not value.strip().lstrip('-').isdigit():
            raise StringContainsNonNumericCharsError()
        return CountAsString(value)
    def value(self)->int:
        try:
            return int(self._value)
        except ValueError:
            raise StringAsIntGetValueError (f"Не возможно преобразовать {self._value} в число")
    def more_zero(self):
        return self.value() > 0
    def __eq__(self, obj: object) -> bool:
        pass


class CountAsFloat(Count):
    _value: float
    def __init__(self, value):
        self._value = value
    @classmethod
    def create(cls, value: float)-> 'Count':
        return CountAsFloat(value)
    def value(self)->float:
        try:
            return float(self._value)
        except ValueError:
            raise CountAsFloatError('Ошибка при создании count из вещественного числа')
    def more_zero(self):
        return self.value() > 0

    def __eq__(self, obj: object) -> bool:
        if not isinstance(obj, Count):
            return False
        other: Count = obj
        return self.value() == other.value()


class CountError(Exception):pass
class StringAsIntError(Exception):pass
class StringNotANumberError(StringAsIntError):pass
class StringAsIntGetValueError(StringAsIntError):pass
class StringContainsNonNumericCharsError(CountError):
    def __init__(self):
        super().__init__(
            f"Не возможно создать строку которая содержит не цифровые символы.")
class CountAsFloatError(CountError):pass
