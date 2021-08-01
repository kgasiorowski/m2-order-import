import src.auth.secret as secret
from src.model.Order.Invoice import Invoice
from src.model.Order.Refund import Refund
from src.model.Order.Order import Order
from src.model.Order.Shipment import Shipment
import requests
from requests.models import Response
import src.auth.auth as auth


class MagentoRequest:
    def __init__(self):
        self.url = secret.url
        self.rest_path = 'rest/default/V1/'
        self.auth_token = auth.get_auth()
        self.headers = {"Content-type": "application/json"}

    def buildBaseRequestUrl(self) -> str:
        return self.url + '/' if not self.url.endswith('/') else self.url + self.rest_path

    def createOrder(self, order: Order, verify=False) -> Response:
        endpoint = self.buildBaseRequestUrl() + 'orders/create'
        return requests.put(
            endpoint,
            order.createRequestData(),
            auth=self.auth_token,
            headers=self.headers,
            verify=verify
        )

    def createInvoice(self, invoice: Invoice, order: Order, item_id_map: dict, verify=False) -> Response:
        endpoint = f"{self.buildBaseRequestUrl()}order/{order.magento_id}/invoice"
        payload = invoice.createRequestData(item_id_map)
        return requests.post(
            endpoint,
            payload,
            auth=self.auth_token,
            headers=self.headers,
            verify=verify
        )

    def createShipment(self, order: Order, shipment: Shipment, verify=False) -> Response:
        ...

    def createRefund(self, order: Order, refund: Refund, verify=False) -> Response:
        ...
