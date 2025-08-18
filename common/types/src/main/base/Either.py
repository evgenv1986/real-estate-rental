from typing import Generic, TypeVar, Callable, Any, Union

L = TypeVar('L')  # Тип для Left
R = TypeVar('R')  # Тип для Right
T = TypeVar('T')  # Общий тип


class Either(Generic[L, R]):
    """Базовый класс Either, от которого наследуются Left и Right"""

    def __init__(self, value: Union[L, R]):
        self.value = value

    def is_left(self) -> bool:
        return isinstance(self, Left)

    def is_right(self) -> bool:
        return isinstance(self, Right)

    def map(self, f: Callable[[R], T]) -> 'Either[L, T]':
        """Применяет функцию к Right значению, игнорирует Left"""
        if self.is_right():
            return Right(f(self.value))
        return self

    def bind(self, f: Callable[[R], 'Either[L, T]']) -> 'Either[L, T]':
        """Монадический bind (>>=)"""
        if self.is_right():
            return f(self.value)
        return self

    def get_or_else(self, default: T) -> Union[R, T]:
        """Возвращает значение Right или default"""
        return self.value if self.is_right() else default

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({repr(self.value)})"


class Left(Either[L, R]):
    """Контейнер для ошибочного значения"""

    def __init__(self, value: L):
        super().__init__(value)


class Right(Either[L, R]):
    """Контейнер для успешного значения"""

    def __init__(self, value: R):
        super().__init__(value)