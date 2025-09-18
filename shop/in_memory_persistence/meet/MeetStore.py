from common.events.src.main.DomainEventPublisher import DomainEventPublisher
from common.types.src.main.base.DomainEntity import DomainEvent
from shop.application.src.main.event.WaitingMessageObjects import WaitingMessageObjects
from shop.domain.src.main.python.meet.Meet import Meet
from shop.usecase.src.tests.meet.access.MeetPersist import MeetPersist

class MeetStore (MeetPersist):
    meets: list[Meet] = []
    waiting_message_entities: WaitingMessageObjects = WaitingMessageObjects()
    def save(self, meet: Meet):
        self.meets.append(meet)
        events: list[DomainEvent] = meet.pop_events()
        self.waiting_message_entities.send(events)

    def __init__(self, waiting_message_entities: WaitingMessageObjects):
        self.waiting_message_entities = waiting_message_entities