from common.types.src.main.common.Count import Count
from shop.domain.src.main.python.advert.advert import Advert
from shop.domain.src.main.python.advert.advert_types import Contact, Address, FloorCount, RoomCount


class TestAdvert():
    def test_create(self):
        assert  Advert.create(
                    contact = Contact('+7...'),
                    address = Address('street', 'house'),
                    floor_count = FloorCount.create_from_str('1'),
                    room_count = RoomCount.create(Count.create('2')),
                    area = '54.0, 56.1',
                    interior = 'евро',
                    flat_floor = '2',
                    cost = '14 800 000',
                    photos = 'imageKitchen, imageRoom',
                    source_advert = 'avito/id=123') \
            .__eq__ (
                Advert.create(
                    contact = Contact('+7...'),
                    address = Address('street', 'house'),
                    floor_count = FloorCount.create_from_str('1'),
                    room_count = RoomCount('2'),
                    area = '54.0, 56.1',
                    interior = 'евро',
                    flat_floor = '2',
                    cost = '14 800 000',
                    photos = 'imageKitchen, imageRoom',
                    source_advert = 'avito/id=123')
            )
        