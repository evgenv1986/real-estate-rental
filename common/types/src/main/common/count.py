from common.types.src.main.base.valueObject import ValueObject
from common.types.src.main.base.valueObject import NegativeValueError


class Count(ValueObject):
    _value: int
    def __init__(self, value):
        self._value = value
    @classmethod
    def create(cls, value: int)-> 'Count':
        if value < 0:
            raise NegativeValueError()
        return Count(value)

    @classmethod
    def create(cls, value: str) -> 'Count':
        if value < 0:
            raise NegativeValueError()
        return Count(value)

    def __init__(self, value: int):
        self._value = value

    def value(self)-> int:
        return self._value

    def more_zero(self):
        return self._value > 0

class StringAsInt(Count):
    _value: str
    def __init__(self, value):
        self._value = value
    @classmethod
    def create(cls, value: str):
        if not value.strip().lstrip('-').isdigit():
            raise StringNotANumberError(f'невозможно создать число из строки {value}')
        return StringAsInt(value)

    def value(self)->int:
        try:
            return int(self._value)
        except ValueError:
            raise StringAsIntGetValueError (f"Не возможно преобразовать {self._value} в число")

    def more_zero(self):
        return self.value() > 0



class StringAsIntError(Exception):pass
class StringNotANumberError(StringAsIntError):pass
class StringAsIntGetValueError(StringAsIntError):pass