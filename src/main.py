import src.io.csv as csv
import src.const.const as const
from src.request.magento_request import MagentoRequest
import warnings
import json


def main():
    request = MagentoRequest()

    for order in csv.generateOrdersFromCsv(const.data_path + const.input_file_name):
        response = request.createOrder(order)
        if response.status_code == 200:
            print(f"Order {order.name} successfully created")
        else:
            error_message = json.loads(response.content.decode())['message']
            if 400 <= response.status_code < 500:
                print(f"Order {order.name} could not be created, there was an error: "
                      f"{response.reason} -> {error_message}")
            elif response.status_code > 500:
                print(f"Order {order.name} could not be created, there was a server error: "
                      f"{response.reason} -> {error_message}")


if __name__ == "__main__":
    warnings.simplefilter('ignore')
    main()
