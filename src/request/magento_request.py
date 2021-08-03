import src.auth.secret as secret
from src.model.Order.Invoice import Invoice
from src.model.Order.Refund import Refund
from src.model.Order.Order import Order
from src.model.Order.Shipment import Shipment
from src.model.AbstractModel import AbstractModel
import requests
from requests.models import Response
import src.auth.auth as auth
import json


class MagentoRequest:

    def __init__(self):
        self.url = secret.url
        self.rest_path = 'rest/default/V1/'

        self.session = requests.Session()
        self.session.headers.update({"Content-type": "application/json"})
        self.session.auth = auth.get_auth()

        self.request_types = {
            "put": self.session.put,
            "post": self.session.post,
            "get": self.session.get
        }

    def buildBaseRequestUrl(self) -> str:
        return self.url + '/' if not self.url.endswith('/') else self.url + self.rest_path

    def createEntity(self,
                     entity: AbstractModel,
                     request_type: str,
                     endpoint: str,
                     verify: bool = False,
                     ) -> Response:

        return self.request_types[request_type](
            endpoint,
            json.dumps(entity.getStructuredPayloadData()),
            verify=verify
        )

    def createOrder(self, order: Order, verify=False) -> Response:
        endpoint = self.buildBaseRequestUrl() + 'orders/create'
        return self.createEntity(
            order,
            "put",
            endpoint,
            verify=verify
        )

    def createInvoice(self, invoice: Invoice, order: Order, verify=False) -> Response:
        endpoint = f"{self.buildBaseRequestUrl()}order/{order.magento_id}/invoice"
        return self.createEntity(
            invoice,
            "post",
            endpoint,
            verify=verify
        )

    def createShipment(self, shipment: Shipment, order: Order, verify=False) -> Response:
        endpoint = f"{self.buildBaseRequestUrl()}order/{order.magento_id}/ship"
        return self.createEntity(
            shipment,
            "post",
            endpoint,
            verify=verify
        )

    def createRefund(self, refund: Refund, order: Order, verify=False) -> Response:
        endpoint = f"{self.buildBaseRequestUrl()}order/{order.magento_id}/refund"
        return self.createEntity(
            refund,
            "post",
            endpoint,
            verify=verify
        )
