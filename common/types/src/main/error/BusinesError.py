from abc import abstractmethod


class BusinessError(Exception):
    @abstractmethod
    def message(self) -> str:pass