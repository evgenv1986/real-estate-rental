import unittest

from shop.persistence.src.main.python.advert.InMemoryAdvertIdProvider import InMemoryAdvertIdProvider


class TestInMemoryAdvertIdProvider(unittest.TestCase):
    def test_last_value(self):
        provider = InMemoryAdvertIdProvider()
        assert 1 == len (provider._list)
        assert 0 == provider._last()
        assert 1 == len (provider._list)

    def test_count_in_list_uid(self):
        provider = InMemoryAdvertIdProvider()
        assert 1 == len (provider._list)
        provider.id()
        assert 2 == len (provider._list)


    def test_next_value(self):
        provider = InMemoryAdvertIdProvider()
        assert 1 == provider.id().value()