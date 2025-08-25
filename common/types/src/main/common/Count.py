from abc import abstractmethod
from typing import Any, TypeVar, Generic

from common.types.src.main.base.ValueObject import ValueObject
from common.types.src.main.base.ValueObject import NegativeValueError

T = TypeVar('T', int, float, str)

# class Count(ValueObject, Generic[T]):
#     def __init__(self, value: T):
#         self.value = value
#     # @abstractmethod
#     def value(self)-> T: pass
#     # @abstractmethod
#     def more_zero(self):
#         pass
#     def __eq__(self, obj: object) -> bool:
#         if not isinstance(obj, Count):
#             return False
#         other: Count = obj
#         return other.value() == self.value()
#     @classmethod
#     def _create_from_str(cls, value: str)-> 'Count':
#         if not value.strip().lstrip('-').isdigit():
#             raise StringContainsNonNumericCharsError()
#         return Count(value)
#     @classmethod
#     def create(cls, value: Any) -> 'Count':
#         if isinstance(value, int):
#             return Count._create_from_int(value)
#         if isinstance(value, str):
#             return Count._create_from_str(value)
#         if isinstance(value, float):
#             return Count._create_from_float(value)
#         raise TypeError(f"не возможно создать Count из {value}")
#     @classmethod
#     def _create_from_float(cls, value: float)-> 'Count':
#         return Count(value)
#     @classmethod
#     def _create_from_int(cls, value: int)-> 'Count':
#         if value < 0:
#             raise NegativeValueError()
#         return Count(value)

class Count(ValueObject):
# class IntCount(Count):
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

#
# class CountAsString(Count):
#     _value: str
#     def __init__(self, value):
#         self._value = value
#     @classmethod
#     def create(cls, value: str):
#         if not value.strip().lstrip('-').isdigit():
#             raise StringContainsNonNumericCharsError()
#         return CountAsString(value)
#     def value(self)->int:
#         try:
#             return int(self._value)
#         except ValueError:
#             raise StringAsIntGetValueError (f"Не возможно преобразовать {self._value} в число")
#     def more_zero(self):
#         return self.value() > 0



# class CountAsFloat(Count):
#     _value: float
#     def __init__(self, value):
#         self._value = value
#     @classmethod
#     def create(cls, value: float)-> 'Count':
#         return CountAsFloat(value)
#     def value(self)->float:
#         try:
#             return float(self._value)
#         except ValueError:
#             raise CountAsFloatError('Ошибка при создании count из вещественного числа')
#     def more_zero(self):
#         return self.value() > 0
#
#     def __eq__(self, obj: object) -> bool:
#         if not isinstance(obj, Count):
#             return False
#         other: Count = obj
#         return self.value() == other.value()


class CountError(Exception):pass
class StringAsIntError(Exception):pass
class StringNotANumberError(StringAsIntError):pass
class StringAsIntGetValueError(StringAsIntError):pass
class StringContainsNonNumericCharsError(CountError):
    def __init__(self):
        super().__init__(
            f"Не возможно создать строку которая содержит не цифровые символы.")
class CountAsFloatError(CountError):pass
