import pytest
from common.types.src.main.common.Count import CountAsString, Count
from shop.domain.src.main.python.advert.Contact import Phone
from shop.domain.src.main.python.advert.advert import Advert
from shop.domain.src.main.python.advert.advert_types import Address, FloorCount, RoomCount, FlatArea, Interior, Price, \
    Photos, Photo, SourceAdvert
from shop.persistence.src.main.python.advert.InMemoryAdvertIdProvider import InMemoryAdvertIdProvider
from shop.usecase.src.main.advert.access.ExtractedAdvert import ExtractedAdvert
from shop.usecase.src.main.advert.invariants.AdvertAlreadyInWorkUseCaseExtracted import \
    AdvertAlreadyInWorkUseCaseExtracted


# class AdvertFixture:
# @pytest.fixture
def advert_with_test_data()-> Advert:
    return Advert(
                contact = Phone('+7...'),
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
                id= InMemoryAdvertIdProvider().next_id()
    )