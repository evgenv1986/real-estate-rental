from common.types.src.main.base.Either import Either, Left, Right
from shop.domain.src.main.python.advert.advert_types import AdvertID
from shop.domain.src.main.python.meet.Meet import Meet
from shop.domain.src.main.python.meet.MeetAt import MeetAt
from shop.domain.src.main.python.meet.MeetIdStore import MeetIdStore
from shop.domain.src.main.python.meet.MeetingTimeNotYetComeCondition import MeetingTimeNotYetComeCondition
from shop.usecase.src.main.advert.access.ExtractedAdvert import ExtractedAdvert
from shop.usecase.src.main.meet.MakeMeet import MakeMeet, MakeMeetUseCaseError
from shop.usecase.src.tests.meet.access.MeetPersist import MeetPersist


class MakeMeetUseCase(MakeMeet):
    def __init__(self,
                 reading_advert_store : ExtractedAdvert,
                 meet_id_store : MeetIdStore,
                 meet_in_future : MeetingTimeNotYetComeCondition,
                 meet_persist : MeetPersist,
                 ):
        self.reading_advert = reading_advert_store
        self.meet_id_store = meet_id_store
        self.meet_in_future = meet_in_future
        self.meet_persist = meet_persist

    def invoke(self, advert_id: AdvertID[int], meet_at: MeetAt) \
            -> Either[MakeMeetUseCaseError, Meet]:
        result = Meet.make(
            self.reading_advert.advert_by_id(advert_id).value,
            meet_at,
            self.meet_id_store,
            self.meet_in_future
        )
        if result.is_left():
            return MakeMeetUseCaseError()
        else:
            meet: Meet = result.value
            self.meet_persist.save(meet)
            return Right(meet)