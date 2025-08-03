from common.types.src.main.base.valueObject import ValueObject

class Contact (ValueObject):
    _telephone: str
    def __init__(self, telephone: str):
        self._telephone = telephone
    def telephone(self):
        return self._telephone


class Address(ValueObject):
    _street: str
    _house: str
    def __init__(self, street, house):
        self._street = street
        self._house = house
