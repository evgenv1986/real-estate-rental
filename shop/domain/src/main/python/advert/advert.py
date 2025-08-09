from common.types.src.main.base.AggregateRoot import AggregateRoot
from common.types.src.main.base.DomainEntity import UID
from shop.domain.src.main.python.advert.advert_types import Contact, Address, FloorCount, \
    RoomCount, AdvertIdProvider, FlatArea


class AdvertEqualsException(Exception):pass




class Advert (AggregateRoot):
    _contact: Contact
    _address: Address
    _floor_count: FloorCount
    _room_count: RoomCount
    _area: FlatArea
    _interior: str
    _flat_floor: str
    _cost: str
    _photos: str
    _source_advert: str
    _id: UID
    
    def __init__(self,
                 contact: Contact,
                 address: Address,
                 floor_count: FloorCount,
                 room_count: RoomCount,
                 area: FlatArea,
                 interior: str,
                 flat_floor: str,
                 cost: str,
                 photos: str,
                 source_advert: str,
                 id: UID):
        
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

    @classmethod
    def create (cls,
                contact: Contact,
                address: Address,
                floor_count: FloorCount,
                room_count: RoomCount,
                area: FlatArea,
                interior: str,
                flat_floor: str,
                cost: str,
                photos: str,
                source_advert: str,
                advert_id_provider: AdvertIdProvider
                ) -> 'Advert':
        advert_id: UID = advert_id_provider.next_id()
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
            advert_id
        )
    
    def contact(self): 
        return self._contact
   
    def __eq__(self, obj: object) -> bool:
        if not isinstance(obj, Advert):
            raise AdvertEqualsException('Ошибка при сравнении объявлений, сравниваемый объект не является классом объявления')
        other: Advert = obj
        return \
            (other.contact().telephone() == self.contact().telephone() and
             other._address.street() == self._address.street() and
             other._address.house() == self._address.house() and
             other._floor_count.value() == self._floor_count.value() and
             other._room_count.value() == self._room_count.value() and
             other._area.living_area().__eq__(self._area.living_area()) and
             other._interior.__eq__(self._interior) and
             other._flat_floor.__eq__(self._flat_floor) and
             other._cost == self._cost
             # and other._photos == self._photos \
             # and other._source_advert == self._source_advert
             )


            