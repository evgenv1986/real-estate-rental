from common.types.src.main.base.AggregateRoot import AggregateRoot
from common.types.src.main.base.DomainEntity import UID
from shop.domain.src.main.python.advert.advert_types import Contact, Address, FloorCount, \
     RoomCount


class AdvertEqualsException(Exception):pass




class Advert (AggregateRoot):
    _contact: Contact
    _address: Address
    _floor_count: FloorCount
    _room_count: RoomCount
    _area: str
    _interior: str
    _flat_floor: str
    _cost: str
    _photos: str
    _source_advert: str
    _id: UID
    
    def __init__(self, contact: Contact, address: Address, floor_count: FloorCount, room_count: RoomCount, area: str,
                 interior: str, flat_floor: str, cost: str, photos: str, source_advert: str, id: UID):
        
        super().__init__(id)
        self._contact = contact
        self._address = address
        self._floor_count = floor_count
        self._room_count = room_count
        self._area = area
        self._interior = interior
        self._flat_floor = flat_floor
        self._cost = cost
        self._photos = photos
        self._source_advert = source_advert
        self._id = id

    @classmethod
    def create (cls,
                contact: Contact,
                address: Address,
                floor_count: FloorCount,
                room_count: RoomCount,
                area: str,
                interior: str,
                flat_floor: str,
                cost: str,
                photos: str,
                source_advert: str,
                id: AdverIdProvider
                ) -> 'Advert':
        return Advert(
            contact,
            address,         
            floor_count,         
            room_count,         
            area,         
            interior,         
            flat_floor,         
            cost,         
            photos,         
            source_advert,
            id
        )
    
    def contact(self): 
        return self._contact
   
    def __eq__(self, obj: object) -> bool:
        if not isinstance(obj, Advert):
            raise AdvertEqualsException('Ошибка при сравнении объявлений, сравниваемый объект не является классом объявления')
        other: Advert = obj
        otherFC: str = other._floor_count.value()
        selfFC: str = self._floor_count.value()
        equalsFC = selfFC == otherFC
        return \
            (other.contact().telephone() == self.contact().telephone() and
             other._address._street == self._address._street and
             other._address._house == self._address._house and
             other._floor_count.value() == self._floor_count.value() and
             other._room_count == self._room_count
            # other._area == self._area \
             # and other._interior == self._interior \
             # and other._flat_floor == self._flat_floor \
             # and other._cost == self._cost \
             # and other._photos == self._photos \
             # and other._source_advert == self._source_advert
             )


            