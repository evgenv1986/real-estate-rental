
from shop.domain.src.main.python.advert.advert_types import AdvertIdProvider, AdvertID


class InMemoryAdvertIdProvider(AdvertIdProvider):
    _list: list[AdvertID] = [AdvertID(0)]
    def __init__(self):
        self._list = [AdvertID[int](0)]

    def next_id(self)-> AdvertID:
        new_id: int = self._last() + 1
        self._list.append( AdvertID(new_id) )
        return AdvertID(self._last())

    def _last(self)-> int:
        if not self._list:
            raise IndexError('list uid is empty')
        return self._list[-1].value()