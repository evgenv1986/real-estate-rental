import unittest

import pytest

from common.types.src.main.common.Count import StringNotANumberError, Count, StringAsInt
from shop.domain.src.main.python.advert.advert_types import FloorCount, FloorCountException, FloorCountLessOrEqualZero, \
    RoomCount


class RoomCountTest(unittest.TestCase):
    def test_error_from_less_zero_room_count_value(self):
        # with pytest.raises(RoomCountLessOrEqualZero):
        #     fc: RoomCount = FloorCount.create_from_str('-1')
        #     assert False == fc.more_zero()
        pass

    def test_error_from_word_char_in_count_value(self):
        count = StringAsInt('1')
        rc: RoomCount = RoomCount.create(count)
        assert True == rc.more_zero()

    def test_equals_created_from_int_and_string(self):
        _str: FloorCount = FloorCount.create_from_str('1')
        _int: FloorCount = FloorCount.create(Count.create(1))
        assert _str.value() == _int.value()