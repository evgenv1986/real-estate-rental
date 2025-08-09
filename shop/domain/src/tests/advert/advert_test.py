import unittest

from common.types.src.main.common.Count import CountAsString, Count
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
                    flat_floor = Count.create(2),
                    price= Price.create(14800000),
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
                    flat_floor=Count.create(2),
                    price=Price.create(14800000),
                    photos=Photos.create([
                        Photo('imageKitchen.jpg'),
                        Photo('imageRoom.jpg')]),
                    source_advert=SourceAdvert('avito/id=123'),
                    advert_id_provider=InMemoryAdvertIdProvider())
            )
    def test_interior(self):
        assert Interior.create('евро').__eq__(Interior.create('евро'))
        assert not Interior.create('xzcnkdcjkd').__eq__(Interior.create('евро'))
    def test_cost(self):
        assert Price.create(14800000).__eq__(Price.create(14800000))
        assert not Price.create(123).__eq__(Price.create(14800000))
    def test_source_advert(self):
        assert not SourceAdvert.create('avito/id=123').__eq__(SourceAdvert.create('avito/id=123000000'))