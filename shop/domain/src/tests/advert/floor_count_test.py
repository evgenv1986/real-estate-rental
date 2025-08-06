import unittest

import pytest

from common.types.src.main.common.Count import StringNotANumberError, Count
from shop.domain.src.main.python.advert.advert_types import FloorCount, FloorCountException, FloorCountLessOrEqualZero


class FloorCountTest(unittest.TestCase):
    def test_error_from_less_zero_floor_count_value(self):
        with pytest.raises(FloorCountLessOrEqualZero):
            fc: FloorCount = FloorCount.create_from_str('-1')
            assert False == fc.more_zero()

    def test_error_from_word_char_in_count_value(self):
        with pytest.raises(StringNotANumberError):
            fc: FloorCount = FloorCount.create_from_str('-1aaa')
            fc.more_zero()

    def test_equals_created_from_int_and_string(self):
        _str: FloorCount = FloorCount.create_from_str('1')
        _int: FloorCount = FloorCount.create(Count.create(1))
        assert _str.value() == _int.value()