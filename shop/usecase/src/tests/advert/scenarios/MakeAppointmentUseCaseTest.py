from datetime import datetime
from typing import List, Any, Type

import pytest

from common.types.src.main.base.Either import Either, Right, Left
from shop.domain.src.main.python.advert.advert import Advert
from shop.domain.src.main.python.advert.advert_types import AdvertID, Address, AdvertIdProvider
from shop.domain.src.main.python.appointment.AppointmentEvents import AppointmentID
from shop.domain.src.teatFixtures.Fixtures import advert_data_fixture, writedonwed_test_advert, \
    writedonwed_test_advert_without_fixture
from shop.in_memory_persistence.InMemoryAdvertRepository import AdvertRepositoryError
from shop.persistence.src.main.python.advert.InMemoryAdvertIdProvider import InMemoryAdvertIdProvider
from shop.domain.src.main.python.appointment.Appointment import Appointment, MeetAt
from shop.usecase.src.main.advert.access.AppointmentIdStore import AppointmentIdStore
from shop.usecase.src.main.advert.access.ExtractedAdvert import ExtractedAdvert, ExtractedAdvertError
from shop.usecase.src.main.advert.scenarios.MakeAppointmentUseCase import MakeAppointmentUseCase


class FakeInMemoryAdvertRepository(ExtractedAdvert):
    _advert: Advert
    def __init__(self, advert: Advert):
        self._advert = advert
    def advert_by_id(self, _id: AdvertID) -> Either[ExtractedAdvertError, Advert]:
        restored_advert: Advert = writedonwed_test_advert_without_fixture()
        restored_advert._id = _id
        if restored_advert.id().value() == _id.value():
            return Right(restored_advert)
        else:
            return Left(ExtractedAdvertError)
    def by_address(self, address: Address) -> Either:pass



class FakeAppointmentIdStore(AppointmentIdStore):
    def provide(self)-> AppointmentID:
        return AppointmentID(1)


class FakeInMemoryAdvertIdProvider(AdvertIdProvider):
    pass


class MeetingTimeNotYetComeCondition:
    pass


class WritingAppointmentStore:
    pass


class FakeExtractingAdvertStorage:
    pass


class TestMakeAppointmentUseCase:
    def test_check_advert_id(self, advert_data_fixture, writedonwed_test_advert):
        assert writedonwed_test_advert.id().value() > 0

    def test_make_appointment(self, advert_data_fixture, writedonwed_test_advert):
        advert = writedonwed_test_advert
        meet_at = datetime.now()
        reading_advert_store: ExtractedAdvert = FakeInMemoryAdvertRepository(advert)
        assert True == reading_advert_store.advert_by_id(advert.id()).is_right()
        restored_advert = reading_advert_store.advert_by_id(advert.id()).value
        assert advert.id().value() == restored_advert.id().value()
        fake_appointment_id_store = FakeAppointmentIdStore()
        appointment_id = fake_appointment_id_store.provide()
        result = MakeAppointmentUseCase(
            reading_advert_store = FakeExtractingAdvertStorage(advert.id()),
            meet_at = MeetAt(meet_at),
            appointment_id_store = fake_appointment_id_store,
            meet_in_future = MeetingTimeNotYetComeCondition(meet_at),
            write_to_storage = WritingAppointmentStore(),
        ).invoke(
            advert.id(),
            meet_at)
        assert True == result.is_right()
        appointment = result.value

        assert meet_at == appointment.meet_at()
        assert advert.id() == appointment.advert_id()
        assert appointment_id == appointment.id()
        assert appointment.contains_event('AppointmentHasBeenMadeDomainEvent')

    def test_list_presented_element(self):
        l: List[str] = ['a', 'b', 'c']
        assert l[0] == 'a'
