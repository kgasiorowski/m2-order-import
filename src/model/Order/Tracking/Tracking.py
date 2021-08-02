from src.model.AbstractModel import AbstractModel


class Tracking(AbstractModel):
    def __init__(self):
        self.title = None
        self.carrier_code = None
        self.tracking_number = None

    def getStructuredPayloadData(self, item_id_map: dict = None) -> dict:
        return {
            "track_number": self.tracking_number,
            "title": self.title,
            "carrier_code": self.carrier_code
        }
