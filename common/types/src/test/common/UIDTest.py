import unittest

from common.types.src.main.common.UID import UID, IntUID


class TestUID(unittest.TestCase):
    def test_uid(self):
        id: UID = IntUID(0)
        assert 0 == id.value()
