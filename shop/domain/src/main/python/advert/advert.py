from common.types.src.main.base.AggregateRoot import AggregateRoot
from common.types.src.main.base.DomainEntity import UID
from common.types.src.main.common.Count import Count
from common.types.src.main.error.BusinesError import BusinessError
from shop.domain import Contact, Address, FloorCount, \
    RoomCount, AdvertIdProvider, FlatArea, SourceAdvert, \
    Photos, Interior, Price, AdvertAlreadyInWork



class Advert (AggregateRoot):
    _contact: Contact
    _address: Address
    _floor_count: FloorCount
    _room_count: RoomCount
    _area: FlatArea
    _interior: Interior
    _flat_floor: Count
    _price: Price
    _photos: Photos
    _source_advert: SourceAdvert
    _id: UID
    #TODO: Заменить тип id: UID, AdvertID классом
    
    def __init__(self,
                 contact: Contact,
                 address: Address,
                 floor_count: FloorCount,
                 room_count: RoomCount,
                 area: FlatArea,
                 interior: Interior,
                 flat_floor: Count,
                 price: Price,
                 photos: Photos,
                 source_advert: SourceAdvert,
                 id: UID):
        
        super().__init__(id)
        self._contact = contact
        self._address = address
        self._floor_count = floor_count
        self._room_count = room_count
        self._area = area
        self._interior = interior
        self._flat_floor = flat_floor
        self._price = price
        self._photos = photos
        self._source_advert = source_advert

    @classmethod
    def create (cls,
                contact: Contact,
                address: Address,
                floor_count: FloorCount,
                room_count: RoomCount,
                area: FlatArea,
                interior: Interior,
                flat_floor: Count,
                price: Price,
                photos: Photos,
                source_advert: SourceAdvert,
                advert_id_provider: AdvertIdProvider,
                advertAlreadyInWork: AdvertAlreadyInWork
                ) -> 'Advert':
        if advertAlreadyInWork.invoke(address):
            AlreadyInWorkAdvertError()
        advert_id: UID = advert_id_provider.next_id()
        return Advert(
            contact,
            address,         
            floor_count,         
            room_count,         
            area,         
            interior,         
            flat_floor,         
            price,
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
             other._price.__eq__(self._price) and
             other._photos.__eq__(self._photos) and
             other._source_advert.__eq__(self._source_advert)
             )
    def id(self) -> UID:
        return self._id



class AdvertEqualsException(Exception):pass


class AlreadyInWorkAdvertError(BusinessError):
    pass
