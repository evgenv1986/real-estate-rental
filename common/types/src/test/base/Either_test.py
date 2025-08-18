import unittest

import pytest

from common.types.src.main.base.Either import Left, Right, Either


class EitherTest(unittest.TestCase):
    def either_right_as_int(self)-> Either[str, int]:
        return Right(1+1)
    def test_right(self):
        result = self.either_right_as_int()
        val = result.value
        self.assertEqual(val, 2)
        self.assertTrue(result.is_right())

    def either_left_as_str(self)-> Either[str, int]:
        return Left("error")
    def test_left(self):
        result = self.either_left_as_str()
        val = result.value
        self.assertEqual(val, "error")
        self.assertTrue(result.is_left())

    def devide_by_zero(self)-> Either[str, float]:
        value = 0
        if value == 0:
            return Left("error devided by zero")
        else:
            return Right(1 / value)
    def test_devide_by_zero(self):
        self.assertTrue (self.devide_by_zero().is_left())

    def devide(self, a: float, b: float) -> Either[str, float]:
        if b == 0:
            return Left("error devided by zero")
        else:
            return Right(a / b)

    def test_devide_is_right(self):
        self.assertTrue (self.devide(2, 2).is_right())
    def test_result_devide(self):
        self.assertTrue (self.devide(2, 2).value == 1)

