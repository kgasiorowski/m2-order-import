import src.auth.secret as secret
from src.model.Refund import Refund
from src.model.Order import Order
from src.model.Invoice import Invoice
from src.model.Shipment import Shipment
from requests.models import Response, Request


class MagentoRequest:
    def __init__(self):
        self.url = secret.url
        self.rest_path = 'rest/default/V1/'


    def buildRequestUrl(self) -> str:
        return self.url + '/' if not self.url.endswith('/') else '' + self.rest_path

    def createOrder(self, order: Order) -> Response:
        ...

    def createInvoice(self, order: Order, invoice: Invoice) -> Response:
        ...

    def createShipment(self, order: Order, shipment: Shipment) -> Response:
        ...

    def createRefund(self, order: Order, refund: Refund) -> Response:
        ...