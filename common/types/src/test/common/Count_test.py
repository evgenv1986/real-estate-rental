import unittest

import pytest

from common.types.src.main.base.ValueObject import NegativeValueError
from common.types.src.main.common.IntCount import CountAsString, StringContainsNonNumericCharsError
from shop.domain.src.main.python.advert.advert_types import IntCount, FloorIntCount


class TestCount(unittest.TestCase):
    def test_cant_create_invalid_count_value(self):
        with pytest.raises(NegativeValueError) as e:
            v: int = -1
            result = IntCount.create(v)

    def test_valid_count_value(self):
        v: int = 2
        count = IntCount(v)
        assert 2 == count.value()

    def test_create_from_srting(self):
        s: str = '1'
        count = CountAsString.create(s)
        assert 1 == count.value()

    def test_cant_create_from_invalid_srting(self):
        s: str = '1sadsd'
        with pytest.raises(StringContainsNonNumericCharsError) as e:
            count = CountAsString.create(s)

