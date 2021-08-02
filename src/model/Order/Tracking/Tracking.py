class Tracking:
    def __init__(self):
        self.title = None
        self.carrier_code = None
        self.tracking_number = None

    def createRequestData(self) -> dict:
        return {
            "track_number": self.tracking_number,
            "title": self.title,
            "carrier_code": self.carrier_code
        }
