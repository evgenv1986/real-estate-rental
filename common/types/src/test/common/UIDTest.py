import unittest

from common.types.src.main.common.UID import UID, IntUID


class TestUID(unittest.TestCase):
    def test_int_uid(self):
        id: UID = IntUID(0)
        assert 0 == id.value()

    def test_uid_as_int(self):
        id: UID = UID(0)
        assert 0 == id.value()

        id1: UID = UID(1)
        assert 1 == id1.value()