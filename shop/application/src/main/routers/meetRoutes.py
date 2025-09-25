from datetime import datetime

from fastapi import APIRouter
import sys
import os

project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
sys.path.append(project_root)

from shop.domain.src.teatFixtures.Fixtures import writedonwed_test_advert_without_fixture

from common.events.src.main.DomainEventListener import SMSMeetMakedRule
from shop.application.src.main.event.WaitingMessageObjects import WaitingMessageObjects
from shop.domain.src.main.python.advert.advert import Advert
from shop.domain.src.main.python.meet.MeetAt import MeetAt
from shop.domain.src.main.python.meet.MeetingTimeNotYetComeCondition import MeetingTimeNotYetComeCondition
from shop.in_memory_persistence.meet.MeetIdStoreInMemory import MeetIdStoreInMemory
from shop.in_memory_persistence.meet.MeetStore import MeetStore
from shop.usecase.src.tests.meet.MakeMeetUseCaseTest import FakeExtractingAdvertStorage

from shop.usecase.src.main.meet.scenarious.MakeMeetUseCase import MakeMeetUseCase
from shop.rest.src.main.meet.MakeMeetEndPoint import MakeMeetEndPoint

router = APIRouter(
    prefix="/api/meets/v1",
    tags=["Meets"]
)

@router.get("/")
async def api_meets_v1():
    advert: Advert = writedonwed_test_advert_without_fixture()
    meet_at = datetime.now()
    waitingMessageObjects = WaitingMessageObjects()
    waitingMessageObjects.register(SMSMeetMakedRule())
    return MakeMeetEndPoint(
        MakeMeetUseCase(
            reading_advert_store=FakeExtractingAdvertStorage(advert.id()),
            meet_id_store=MeetIdStoreInMemory(),
            meet_in_future=MeetingTimeNotYetComeCondition(MeetAt(meet_at)),
            meet_persist=MeetStore(waitingMessageObjects),
        )
    ).execute(
        advert.id().value(),
        meet_at
    )
    # return {"message": "Meets endpoint324234324"}