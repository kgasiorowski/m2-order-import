import abc


class AbstractModel(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def getStructuredPayloadData(self, item_id_map: dict = None) -> dict:
        ...