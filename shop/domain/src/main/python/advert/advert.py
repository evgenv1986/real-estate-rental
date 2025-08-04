from shop.domain.src.main.python.advert.advert_types import Contact, Address, Count, FloorCount, \
    FloorCountLessOrEqualZero


class AdvertEqualsException(Exception):pass


class Advert:
    _contact: Contact
    _address: Address
    _floor_count: FloorCount
    _room_count: str
    _area: str
    _interior: str
    _flat_floor: str
    _cost: str
    _photos: str
    _source_advert: str
    
    def __init__(self,
                    contact: Contact,
                    address: str,
                    floor_count: FloorCount,
                    room_count: str,
                    area: str,
                    interior: str,
                    flat_floor: str,
                    cost: str,
                    photos: str,
                    source_advert: str):
        
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
                room_count: str,
                area: str,
                interior: str,
                flat_floor: str,
                cost: str,
                photos: str,
                source_advert: str
                ) -> 'Advert':
        if not floor_count.more_zero():
            raise FloorCountLessOrEqualZero()
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
            source_advert)
    
    def contact(self): 
        return self._contact
   
    def __eq__(self, obj: object) -> bool:
        if not isinstance(obj, Advert):
            raise AdvertEqualsException('Ошибка при сравнении объявлений, сравниваемый объект не является классом объявления')
        other: Advert = obj
        return \
            other.contact().telephone() == self.contact().telephone() and \
            other._address._street == self._address._street and \
            other._address._house == self._address._house

            