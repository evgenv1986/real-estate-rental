import unittest

from common.types.src.main.common.Count import CountAsString, IntCount
from shop.domain.src.main.python.advert.advert import Advert
from shop.domain.src.main.python.advert.advert_types import Contact, Address, FloorCount, RoomCount, FlatArea, Interior, \
    Price, Photo, Photos, SourceAdvert
from shop.persistence.src.main.python.advert.InMemoryAdvertIdProvider import InMemoryAdvertIdProvider


class TestAdvert(unittest.TestCase):
    def test_create(self):
        advert = Advert.create(
                    contact = Contact('+7...'),
                    address = Address('street', 'house'),
                    floor_count = FloorCount.create_from_str('1'),
                    room_count = RoomCount.create(CountAsString.create('2')),
                    area = FlatArea.create(
                        living_area = 54.0,
                        total_area = 56.1),
                    interior = Interior.create('евро'),
                    flat_floor = IntCount(2),
                    cost = Price.create(14800000),
                    photos = Photos.create([
                            Photo('imageKitchen.jpg'),
                            Photo('imageRoom.jpg')]),
                    source_advert = SourceAdvert('avito/id=123'),
                    advert_id_provider = InMemoryAdvertIdProvider())
        assert advert.__eq__ (
                Advert.create(
                    contact = Contact('+7...'),
                    address = Address('street', 'house'),
                    floor_count = FloorCount.create_from_str('1'),
                    room_count = RoomCount.create(CountAsString.create('2')),
                    area = FlatArea.create(
                        living_area = 54.0,
                        total_area = 56.1),
                    interior = Interior.create('евро'),
                    flat_floor = '2',
                    cost = '14 800 000',
                    photos = 'imageKitchen, imageRoom',
                    source_advert = 'avito/id=123',
                    advert_id_provider = InMemoryAdvertIdProvider())
            )
    def test_interior(self):
        assert Interior.create('евро').__eq__(Interior.create('евро'))
