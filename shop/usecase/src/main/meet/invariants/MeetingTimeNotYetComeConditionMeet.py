from datetime import datetime

from shop.domain.src.main.python.meet.Appointment import MeetAt
from shop.domain.src.main.python.meet.MeetingTimeNotYetComeCondition import MeetingTimeNotYetComeCondition

class MeetingTimeNotYetComeConditionMeet (MeetingTimeNotYetComeCondition):
    def __init__(self, today: datetime):
        self.today = today
    def invoke(self, meetAt: MeetAt):
        return self.today <= meetAt.value

