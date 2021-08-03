import src.auth.secret as secret
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

        # Determines what endpoint and which function each entity type needs.
        self.entity_types = {
            'order': ('orders/create', self.session.put),
            'invoice':  ('order/{}/invoice', self.session.post),
            'shipment': ('order/{}/ship', self.session.post),
            'refund': ('order/{}/refund', self.session.post)
        }

    def buildBaseRequestUrl(self) -> str:
        return self.url + '/' if not self.url.endswith('/') else self.url + self.rest_path

    def createEntity(
        self,
        entity: AbstractModel,
        entity_type: str,
        order_id: int = None,
        verify: bool = False,
    ) -> Response:

        # Build our endpoint
        endpoint = self.buildBaseRequestUrl()
        endpoint += self.entity_types[entity_type][0]
        endpoint = endpoint.format(order_id if order_id is not None else '')

        # Generate our payload
        payload = json.dumps(entity.getStructuredPayloadData())

        # Extract the request function to use (put, post, get, etc)
        request_function = self.entity_types[entity_type][1]

        # Perform the request
        return request_function(
            endpoint,
            payload,
            verify=verify
        )
