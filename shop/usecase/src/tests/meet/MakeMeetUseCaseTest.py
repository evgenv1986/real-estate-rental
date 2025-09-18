from datetime import datetime
from typing import List, Any, Type

from common.events.src.main.DomainEventListener import SMSMeetMakedRule
from common.types.src.main.base.Either import Either, Right, Left
from shop.application.src.main.event.WaitingMessageObjects import WaitingMessageObjects
from shop.domain.src.main.python.advert.advert import Advert
from shop.domain.src.main.python.advert.advert_types import AdvertID, Address, AdvertIdProvider
from shop.domain.src.main.python.meet.Meet import Meet
from shop.domain.src.main.python.meet.MeetAt import MeetAt
from shop.domain.src.main.python.meet.MeetEvents import MeetMakedEvent
from shop.domain.src.main.python.meet.MeetingTimeNotYetComeCondition import MeetingTimeNotYetComeCondition
from shop.domain.src.teatFixtures.Fixtures import advert_data_fixture, writedonwed_test_advert, \
    writedonwed_test_advert_without_fixture
from shop.in_memory_persistence.meet.MeetIdStoreInMemory import MeetIdStoreInMemory
from shop.in_memory_persistence.meet.MeetStore import MeetStore
from shop.usecase.src.main.advert.access.ExtractedAdvert import ExtractedAdvert, ExtractedAdvertError
from shop.usecase.src.main.meet.scenarious.MakeMeetUseCase import MakeMeetUseCase


class FakeInMemoryAdvertRepository(ExtractedAdvert):
    _advert: Advert
    def __init__(self, advert: Advert):
        self._advert = advert
    def advert_by_id(self, _id: AdvertID) -> Right[Any, Advert] | Left[Type[ExtractedAdvertError], Any]:
        restored_advert: Advert = writedonwed_test_advert_without_fixture()
        restored_advert._id = _id
        if restored_advert.id().value() == _id.value():
            return Right(restored_advert)
        else:
            return Left(ExtractedAdvertError)
    def by_address(self, address: Address) -> Either:pass




class FakeInMemoryAdvertIdProvider(AdvertIdProvider):
    def next_id(self) -> 'AdvertID':
        pass


class FakeExtractingAdvertStorage(ExtractedAdvert):
    def __init__(self, advert_id: AdvertID[int]):
        self._advert_id = advert_id
    def by_address(self, address: Address) -> Either:pass
    def advert_by_id(self, _id: AdvertID)-> Either['ExtractedAdvertError', Advert]:
        advert: Advert = writedonwed_test_advert_without_fixture()
        return Right(advert)



class TestMakeAppointmentUseCase:
    def test_check_advert_id(self, advert_data_fixture, writedonwed_test_advert):
        assert writedonwed_test_advert.id().value() > 0

    def test_meet_make(self, advert_data_fixture, writedonwed_test_advert):
        advert = writedonwed_test_advert
        meet_at = datetime.now()
        reading_advert_store: ExtractedAdvert = FakeInMemoryAdvertRepository(advert)
        assert True == reading_advert_store.advert_by_id(advert.id()).is_right()
        restored_advert = reading_advert_store.advert_by_id(advert.id()).value
        assert advert.id().value() == restored_advert.id().value()
        fake_meet_id_store = MeetIdStoreInMemory()
        meet_id = fake_meet_id_store.new_id()
        waiting_message_entities = WaitingMessageObjects()
        sms_meet_maked_rule = SMSMeetMakedRule()
        waiting_message_entities.register(sms_meet_maked_rule)
        result: Either = MakeMeetUseCase(
            reading_advert_store = FakeExtractingAdvertStorage(advert.id()),
            meet_id_store= MeetIdStoreInMemory(),
            meet_in_future = MeetingTimeNotYetComeCondition(MeetAt(meet_at)),
            meet_persist= MeetStore(waiting_message_entities),
        ).invoke(
            advert.id(),
            MeetAt(meet_at))
        assert True == result.is_right()
        meet: Meet = result.value

        assert meet_at == meet._meet_at.value
        assert advert.id()._id == meet._advert_id._id
        assert meet_id == meet.id()
        assert isinstance(sms_meet_maked_rule.event, MeetMakedEvent)

    def test_list_presented_element(self):
        l: List[str] = ['a', 'b', 'c']
        assert l[0] == 'a'
    def test_meet_at_not_empty(self):
        dt = datetime.now()
        assert MeetAt(dt).value == dt
    def test_meet_id_store_generated_id(self):
        fake_meet_id_store = MeetIdStoreInMemory()
        meet_id = fake_meet_id_store.new_id()
        assert None != meet_id