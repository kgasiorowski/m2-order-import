import abc


class AbstractModel(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def getStructuredPayloadData(self) -> dict:
        ...
