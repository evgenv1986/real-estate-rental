from common.types.src.main.base.DomainEntity import UID
from common.types.src.main.common.UID import IntUID
from shop.domain.src.main.python.advert.advert_types import AdverIdProvider


class InMemoryAdvertIdProvider(AdverIdProvider):
    _list: list[UID]
    def __init__(self):
        self._list = [IntUID(0)]

    def id(self)-> UID:
        self._list.append(
            IntUID(self._last().value() + 1))
        return IntUID(self._last().value())

    def _last(self)-> IntUID:
        if not self._list:
            raise IndexError('list uid is empty')
        return self._list[-1].value()