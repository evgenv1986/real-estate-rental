import pytest

from common.events.src.tests.TestPublisher import TestPublisher
from common.types.src.main.common.Count import Count
from shop.domain.src.main.python.advert.Contact import Phone
from shop.domain.src.main.python.advert.advert import Advert
from shop.domain.src.main.python.advert.advert_types import Address, FloorCount, RoomCount, FlatArea, Interior, Price, \
    Photos, Photo, SourceAdvert
from shop.in_memory_persistence.InMemoryAdvertRepository import InMemoryAdvertRepository
from shop.persistence.src.main.python.advert.InMemoryAdvertIdProvider import InMemoryAdvertIdProvider
from shop.usecase.src.main.advert.TakeAdvertToWork import AdvertData
from shop.usecase.src.main.advert.access.ExtractedAdvert import ExtractedAdvert
from shop.usecase.src.main.advert.invariants.AdvertAlreadyInWorkUseCaseExtracted import \
    AdvertAlreadyInWorkUseCaseExtracted
from shop.usecase.src.main.advert.invariants.AdvertRejectedStoredUseCase import AdvertRejectedStoredUseCase


@pytest.fixture
def writedonwed_test_advert()-> Advert:
    return Advert.write_down(
                contact = Phone('+7...'),
                address = Address('street', 'house'),
                floor_count = FloorCount.create(1),
                room_count = RoomCount.create(Count.create(2)),
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
                advert_id_provider = InMemoryAdvertIdProvider(),
                advert_already_in_work=
                    AdvertAlreadyInWorkUseCaseExtracted(
                        InMemoryAdvertRepository(
                            TestPublisher())),
                advert_rejected= AdvertRejectedStoredUseCase(
                    InMemoryAdvertRepository(
                        TestPublisher()))
    )

@pytest.fixture(scope='function')
def advert_data_fixture()-> AdvertData:
    return AdvertData(
        contact=Phone('+7...'),
        address=Address('street', 'house'),
        floor_count=FloorCount.create(1),
        room_count=RoomCount.create(Count.create(2)),
        area=FlatArea.create(
            living_area=54.0,
            total_area=56.1),
        interior=Interior.create('евро'),
        flat_floor=Count.create(2),
        price=Price.create(14800000),
        photos=Photos.create([
            Photo('imageKitchen.jpg'),
            Photo('imageRoom.jpg')]),
        source_advert=SourceAdvert('avito/id=123'),
    )

def writedonwed_test_advert_without_fixture()-> Advert:
    return Advert.write_down(
                contact = Phone('+7...'),
                address = Address('street', 'house'),
                floor_count = FloorCount.create(1),
                room_count = RoomCount.create(Count.create(2)),
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
                advert_id_provider = InMemoryAdvertIdProvider(),
                advert_already_in_work=
                    AdvertAlreadyInWorkUseCaseExtracted(
                        InMemoryAdvertRepository(
                            TestPublisher())),
                advert_rejected= AdvertRejectedStoredUseCase(
                    InMemoryAdvertRepository(
                        TestPublisher()))
    )