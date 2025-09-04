from datetime import datetime
from typing import List, Any, Type

import pytest

from common.types.src.main.base.Either import Either, Right, Left
from shop.domain.src.main.python.advert.advert import Advert
from shop.domain.src.main.python.advert.advert_types import AdvertID, Address
from shop.domain.src.teatFixtures.Fixtures import advert_data_fixture, writedonwed_test_advert, \
    writedonwed_test_advert_without_fixture
from shop.in_memory_persistence.InMemoryAdvertRepository import AdvertRepositoryError
from shop.persistence.src.main.python.advert.InMemoryAdvertIdProvider import InMemoryAdvertIdProvider
from shop.domain.src.main.python.appointment.Appointment import Appointment
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


class TestMakeAppointmentUseCase:
    def test_make_appointment(self, advert_data_fixture, writedonwed_test_advert):
        advert_data = advert_data_fixture
        advert_id_provider = InMemoryAdvertIdProvider()
        advert = writedonwed_test_advert
        _id = advert_id_provider.next_id()
        meet_at = datetime.now()

        repository = FakeInMemoryAdvertRepository(advert)
        restored_advert = repository.advert_by_id(_id)

        # restored_advert = repository.advert_by_id(advert.id())
        make_appointment = MakeAppointmentUseCase(repository)
        either: Either = make_appointment.invoke(_id, meet_at)
        appointment: Appointment = either.value
        assert meet_at == appointment.meet_at()
        assert _id == appointment.advert_id()
        assert appointment.contains_event('AppointmentHasBeenMadeDomianEvent')

    def test_list_presented_element(self):
        l: List[str] = ['a', 'b', 'c']
        assert l[0] == 'a'
