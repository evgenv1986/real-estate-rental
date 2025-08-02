import pytest

# from shop.domain.src.main.python.advert.advert import Advert
from main.python.advert.advert import Advert

class TestAdvert:
    def test_initial(self):
        assert  Advert.create(
                    contact = '+7...',
                    address = 'street, house',
                    floor_count = '9',
                    room_count = '2',
                    area = '54.0, 56.1',
                    interior = 'евро',
                    flat_floor = '2',
                    cost = '14 800 000',
                    photos = 'imageKitchen, imageRoom',
                    source_advert = 'avito/id=123') \
            .__eq__ (
                Advert.create(
                    contact = '+7...',
                    address = 'street, house',
                    floor_count = '9',
                    room_count = '2',
                    area = '54.0, 56.1',
                    interior = 'евро',
                    flat_floor = '2',
                    cost = '14 800 000',
                    photos = 'imageKitchen, imageRoom',
                    source_advert = 'avito/id=123')
            )