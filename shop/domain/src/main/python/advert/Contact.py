from abc import ABC, abstractmethod
from typing import final, ClassVar, FrozenSet
from dataclasses import dataclass

from common.types.src.main.base.ValueObject import ValueObject

class Contact(ValueObject):
    """Базовый запечатанный класс для контактов"""
    _allowed_subclasses: ClassVar[FrozenSet[str]] = frozenset({'Phone', 'Email'})

    def __init_subclass__(cls, **kwargs):
        if cls.__name__ not in Contact._allowed_subclasses:
            raise TypeError(f"Cannot subclass {cls.__name__}. Contact is sealed.")
        super().__init_subclass__(**kwargs)
    def value(self):pass

# Разрешённые подклассы
@dataclass
class Phone(Contact):
    number: str
    def value(self):
        return self.number


@dataclass
class Email(Contact):
    address: str
    def value(self):
        return self.address

