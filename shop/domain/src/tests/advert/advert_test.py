import unittest

from common.types.src.main.common.Count import Count
from shop.domain.src.main.python.advert.Contact import Contact, Phone, Email
from shop.domain.src.main.python.advert.advert import Advert
from shop.domain.src.main.python.advert.advert_types import Address, FloorCount, RoomCount, FlatArea, Interior, Price, \
    Photos, Photo, SourceAdvert
from shop.in_memory_persistence.InMemoryAdvertRepository import InMemoryAdvertRepository
from common.events.src.tests.TestPublisher import TestPublisher
from shop.persistence.src.main.python.advert.InMemoryAdvertIdProvider import InMemoryAdvertIdProvider
from shop.usecase.src.main.advert.invariants.AdvertAlreadyInWorkUseCaseExtracted import \
    AdvertAlreadyInWorkUseCaseExtracted
from shop.usecase.src.main.advert.invariants.AdvertRejectedStoredUseCase import AdvertRejectedStoredUseCase


class TestAdvert(unittest.TestCase):
    def test_create(self):
        advert = Advert.write_down(
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
                            InMemoryAdvertRepository(TestPublisher())
                        ),
                    advert_rejected= AdvertRejectedStoredUseCase(
                        InMemoryAdvertRepository(
                            TestPublisher()))
        )
        assert advert.__eq__ (
                Advert.write_down(
                    contact = Phone('+7...'),
                    address = Address('street', 'house'),
                    floor_count = FloorCount.create(1),
                    room_count = RoomCount.create(Count.create(2)),
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
                    advert_id_provider=InMemoryAdvertIdProvider(),
                    advert_already_in_work= AdvertAlreadyInWorkUseCaseExtracted(
                        InMemoryAdvertRepository(TestPublisher())
                    ),
                    advert_rejected= AdvertRejectedStoredUseCase(
                        InMemoryAdvertRepository(
                            TestPublisher()))
            ))
    def test_interior(self):
        assert Interior.create('евро').__eq__(Interior.create('евро'))
        assert not Interior.create('xzcnkdcjkd').__eq__(Interior.create('евро'))
    def test_cost(self):
        assert Price.create(14800000).__eq__(Price.create(14800000))
        assert not Price.create(123).__eq__(Price.create(14800000))
    def test_source_advert(self):
        assert not SourceAdvert.create('avito/id=123').__eq__(SourceAdvert.create('avito/id=123000000'))
    def test_contact(self):
        Phone('+7')
        Email('<EMAIL>')
        try:
            class Telegram(Contact):  # Вызовет TypeError
                pass
        except TypeError as e:
            print(e)  # Cannot subclass Telegram. Contact is sealed.

    def test_advert_rejected(self):
        advert_rejected = AdvertRejectedStoredUseCase(
            InMemoryAdvertRepository(
                TestPublisher()))
        self.assertFalse (advert_rejected.invoke (Address('street', 'house')))




























