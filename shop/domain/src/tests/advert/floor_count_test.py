import unittest

import pytest

from common.types.src.main.common.Count import StringNotANumberError
from shop.domain.src.main.python.advert.advert_types import FloorCount, FloorCountException, FloorCountLessOrEqualZero


class FloorCountTest(unittest.TestCase):
    def test_error_from_less_zero_floor_count_value(self):
        with pytest.raises(FloorCountLessOrEqualZero):
            fc: FloorCount = FloorCount.createFromStr('-1')
            assert False == fc.more_zero()

    def test_error_from_word_char_in_count_value(self):
        with pytest.raises(StringNotANumberError):
            fc: FloorCount = FloorCount.createFromStr('-1aaa')
            fc.more_zero()