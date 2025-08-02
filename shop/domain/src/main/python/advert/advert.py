class Advert:
    @classmethod
    def create (cls, 
                contact: str,
                address: str,
                floor_count: str,
                room_count: str,
                area: str,
                interior: str,
                flat_floor: str,
                cost: str,
                photos: str,
                source_advert: str
                ) -> 'Advert':
        return Advert()
    def __eq__(self, other: object) -> bool:
        return True