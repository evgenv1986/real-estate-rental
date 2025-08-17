from common.types.src.main.base.ValueObject import ValueObject


class Contact (ValueObject):
    _telephone: str
    def __init__(self, telephone: str):
        self._telephone = telephone
    def telephone(self):
        return self._telephone
