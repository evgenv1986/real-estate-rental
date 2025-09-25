from shop.usecase.src.main.meet.MakeMeet import MakeMeet

class MakeMeetEndPoint:
    def __init__(self, make_meet: MakeMeet):
        self.make_meet = make_meet
    def execute(self):pass