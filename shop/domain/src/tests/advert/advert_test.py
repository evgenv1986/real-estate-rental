from common.types.src.main.common.Count import Count
from shop.domain.src.main.python.advert.Contact import Contact, Phone, Email
from shop.domain.src.main.python.advert.advert import Advert
from shop.domain.src.main.python.advert.advert_types import Address, FloorCount, RoomCount, FlatArea, Interior, Price, \
    Photos, Photo, SourceAdvert, AdvertState, AdvertIdleState, AdvertWritedownedState
from shop.in_memory_persistence.InMemoryAdvertRepository import InMemoryAdvertRepository
from common.events.src.tests.TestPublisher import TestPublisher
from shop.persistence.src.main.python.advert.InMemoryAdvertIdProvider import InMemoryAdvertIdProvider
from shop.usecase.src.main.advert.invariants.AdvertAlreadyInWorkUseCaseExtracted import \
    AdvertAlreadyInWorkUseCaseExtracted
from shop.usecase.src.main.advert.invariants.AdvertRejectedStoredUseCase import AdvertRejectedStoredUseCase
from shop.domain.src.teatFixtures.Fixtures import advert_data_fixture



class TestAdvert:
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
        assert False == (advert_rejected.invoke (Address('street', 'house')))

    def test_change_state_to_writedowned(self, advert_data_fixture):
        d = advert_data_fixture
        advert: Advert = Advert(
            d.contact,
            d.address,
            d.floor_count,
            d.room_count,
            d.area,
            d.interior,
            d.flat_floor,
            d.price,
            d.photos,
            d.source_advert,
            _id=InMemoryAdvertIdProvider().next_id()
        )
        writedowned_advert = advert.write_down(
            d.contact,
            d.address,
            d.floor_count,
            d.room_count,
            d.area,
            d.interior,
            d.flat_floor,
            d.price,
            d.photos,
            d.source_advert,
            advert_id_provider=InMemoryAdvertIdProvider(),
            advert_already_in_work = AdvertAlreadyInWorkUseCaseExtracted(
                InMemoryAdvertRepository(TestPublisher())),
            advert_rejected=AdvertRejectedStoredUseCase(
                InMemoryAdvertRepository(TestPublisher()))
        )
        assert True == isinstance (writedowned_advert._state, AdvertWritedownedState)

    def test_writedowned_state(self, advert_data_fixture):
        idle: AdvertState = AdvertIdleState()
        assert AdvertWritedownedState == idle.next_state()

    def test_can_change_to_state(self):
        ns = AdvertIdleState().next_state()
        can = AdvertIdleState().canChangeTo(AdvertWritedownedState())
        assert (True == AdvertIdleState()
                .canChangeTo(AdvertWritedownedState()))
        assert (False == AdvertIdleState()
                .canChangeTo(AdvertIdleState()))

    def test_equals_classes(self):
        assert (True == isinstance(AdvertWritedownedState(), AdvertWritedownedState))













