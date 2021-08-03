from src.model.Order.Item import Item
from src.model.Order.Tracking.Tracking import Tracking
from src.model.AbstractModel import AbstractModel


class Shipment(AbstractModel):
    def __init__(self, original_id: int):
        self.id = original_id
        self.items = []
        self.tracks = []

    def addItem(self, item: Item):
        self.items.append(item)

    def addTrack(self, track: Tracking):
        self.tracks.append(track)

    def getStructuredPayloadData(self) -> dict:
        return {
            "items": [item.getSubRequestFormattedData() for item in self.items],
            "tracks": [track.getStructuredPayloadData() for track in self.tracks]
        }
