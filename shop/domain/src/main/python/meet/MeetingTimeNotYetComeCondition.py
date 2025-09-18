from shop.domain.src.main.python.meet.MeetAt import MeetAt


class MeetingTimeNotYetComeCondition:
    def __init__(self, meet_at: MeetAt):
        self.meet_at = meet_at
    def invoke(self, meetAt: MeetAt)->bool:
        return meetAt.value <= self.meet_at.value
