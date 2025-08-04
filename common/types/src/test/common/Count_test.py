import unittest
from unittest.result import failfast

import pytest

from common.types.src.main.common.count import FloorCountLessOrEqualZero
from shop.domain.src.main.python.advert.advert_types import Count, FloorCount


class TestCount(unittest.TestCase):
    def test_cant_create_invalid_count_value(self):
        v: int = -1
        result = Count.create(v)

    def test_valid_count_value(self):
        v: int = 2
        count = Count(v)
        assert True == count.valid()

    def test_error_from_invalid_count_value(self):
        v: int = -1
        count = Count(v)
        assert False == count.value()

