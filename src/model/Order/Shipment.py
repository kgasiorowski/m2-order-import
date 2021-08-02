from src.model.Order.Item import Item
from src.model.Order.Tracking.Tracking import Tracking
import json


class Shipment:
    def __init__(self, original_id: int):
        self.id = original_id
        self.items = []
        self.tracks = []

    def addItem(self, item: Item):
        self.items.append(item)

    def addTrack(self, track: Tracking):
        self.tracks.append(track)

    def createRequestData(self, item_id_map: dict) -> str:
        items = []
        for item in self.items:
            items.append(item.createRequestData(item_id_map))

        tracks = []
        for track in self.tracks:
            tracks.append(track.createRequestData())

        payload = {
            "items": items,
            "tracks": tracks
        }
        return json.dumps(payload)
