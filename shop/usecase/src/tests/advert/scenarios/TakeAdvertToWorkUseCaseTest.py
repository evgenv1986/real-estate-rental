import pytest

from common.events.src.tests.TestPublisher import TestPublisher
from shop.domain.src.teatFixtures.Fixtures import writedonwed_test_advert, advert_data_fixture
from shop.in_memory_persistence.InMemoryAdvertRepository import InMemoryAdvertRepository
from shop.persistence.src.main.python.advert.InMemoryAdvertIdProvider import InMemoryAdvertIdProvider
from shop.usecase.src.main.advert.TakeAdvertToWork import TakeAdvertToWork
from shop.usecase.src.main.advert.invariants.AdvertAlreadyInWorkUseCaseExtracted import \
    AdvertAlreadyInWorkUseCaseExtracted
from shop.usecase.src.main.advert.invariants.AdvertRejectedStoredUseCase import AdvertRejectedStoredUseCase
from shop.usecase.src.main.advert.scenarios.TakeAdvertToWorkUseCase import TakeAdvertToWorkUseCase


class TestTakeAdvertToWorkUseCase():
    def test_taked_to_work_success(self, advert_data_fixture):
        advert_data = advert_data_fixture
        usecase: TakeAdvertToWork = TakeAdvertToWorkUseCase(
            advertIdProvider = InMemoryAdvertIdProvider(),
            advertAlreadyInWork = AdvertAlreadyInWorkUseCaseExtracted(
                InMemoryAdvertRepository(TestPublisher())
            ),
            advert_persist = InMemoryAdvertRepository(TestPublisher()),
            advert_rejected = AdvertRejectedStoredUseCase(
                            InMemoryAdvertRepository(TestPublisher()))
        )
        usecase.invoke(advert_data)
