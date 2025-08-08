from common.types.src.main.common.IntCount import IntCount
from shop.domain.src.main.python.advert.advert import Advert
from shop.domain.src.main.python.advert.advert_types import Contact, Address, FloorIntCount, RoomIntCount
from shop.persistence.src.main.python.advert.InMemoryAdvertIdProvider import InMemoryAdvertIdProvider


class TestAdvert():
    def test_create(self):
        advert = Advert.create(
                    contact = Contact('+7...'),
                    address = Address('street', 'house'),
                    floor_count = FloorIntCount.create_from_str('1'),
                    room_count = RoomIntCount.create(IntCount.create('2')),
                    area = '54.0, 56.1',
                    interior = 'евро',
                    flat_floor = '2',
                    cost = '14 800 000',
                    photos = 'imageKitchen, imageRoom',
                    source_advert = 'avito/id=123',
                    advert_id_provider = InMemoryAdvertIdProvider())
        assert advert.__eq__ (
                Advert.create(
                    contact = Contact('+7...'),
                    address = Address('street', 'house'),
                    floor_count = FloorIntCount.create_from_str('1'),
                    room_count = RoomIntCount.create(IntCount.create('2')),
                    area = '54.0, 56.1',
                    interior = 'евро',
                    flat_floor = '2',
                    cost = '14 800 000',
                    photos = 'imageKitchen, imageRoom',
                    source_advert = 'avito/id=123',
                    advert_id_provider = InMemoryAdvertIdProvider())
            )
        