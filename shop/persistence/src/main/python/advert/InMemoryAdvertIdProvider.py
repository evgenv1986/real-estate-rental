from common.types.src.main.base.DomainEntity import UID

from shop.domain.src.main.python.advert.advert_types import AdvertIdProvider, AdvertID


class InMemoryAdvertIdProvider(AdvertIdProvider):
    _list: list[AdvertID]
    def __init__(self):
        self._list = [AdvertID[int](0)]

    def next_id(self)-> UID:
            # last_value = self._last().value()
            # new_uid = UID[int](last_value + 1)
            # self._list.append(new_uid)
        # В моем коде проблема для компилятора - Expected type 'int', got 'UID' instead
        # зато он кратче """
        self._list.append(AdvertID[int](self._last() + 1))
        return UID[int](self._last())

    def _last(self)-> AdvertID:
        if not self._list:
            raise IndexError('list uid is empty')
        return self._list[-1].value()