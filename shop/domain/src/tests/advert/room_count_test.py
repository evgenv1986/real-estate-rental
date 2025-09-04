import unittest

import pytest

from common.types.src.main.common.Count import StringNotANumberError, IntCount, CountAsString
from shop.domain.src.main.python.advert.advert_types import FloorCountException, FloorCountLessOrEqualZero, \
    RoomCount, FloorCount, RoomCountLessOrEqualZero


class RoomCountTest(unittest.TestCase):
    def test_error_from_less_zero_room_count_value(self):
        with pytest.raises(RoomCountLessOrEqualZero):
            rc: RoomCount = RoomCount.create(CountAsString.make('-1'))


    def test_error_from_word_char_in_count_value(self):
        count = CountAsString.make('1')
        rc: RoomCount = RoomCount.create(count)
        assert True == rc.more_zero()

    def test_equals_created_from_int_and_string(self):
        _str: RoomCount = RoomCount.create(CountAsString.make('1'))
        _int: RoomCount = RoomCount.create(IntCount.make(1))
        assert _str.value() == _int.value()