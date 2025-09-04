import unittest

import pytest

from common.types.src.main.base.ValueObject import NegativeValueError
from common.types.src.main.common.Count import CountAsString, StringContainsNonNumericCharsError, Count
from shop.domain.src.main.python.advert.advert_types import IntCount


class TestCount(unittest.TestCase):
    def test_cant_create_invalid_count_value(self):
        with pytest.raises(NegativeValueError):
            v: int = -1
            IntCount.make(v)

    def test_valid_count_value(self):
        v: int = 2
        count = IntCount(v)
        assert 2 == count.value()

    def test_create_from_srting(self):
        s: str = '1'
        count = CountAsString.make(s)
        assert 1 == count.value()

    def test_cant_create_from_invalid_srting(self):
        s: str = '1sadsd'
        with pytest.raises(StringContainsNonNumericCharsError):
            CountAsString.make(s)

    def test_create_IntCount_with_Count_class(self):
        assert Count.create(234).__eq__(Count.create(234))

    def test_create_StringCount_with_Count_class(self):
        assert Count.create("234").__eq__(Count.create("234"))

    def test_create_FloatCount_with_Count_class(self):
        assert Count.create(1.23).__eq__(Count.create(1.23))