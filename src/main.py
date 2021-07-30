import src.io.csv as csv
import src.const.const as const
from src.request.magento_request import MagentoRequest
import warnings


def main():

    request = MagentoRequest()

    for order in csv.generateOrdersFromCsv(const.data_path + const.input_file_name):
        response = request.createOrder(order)
        print(response.status_code)


if __name__ == "__main__":
    warnings.simplefilter('ignore')
    main()
