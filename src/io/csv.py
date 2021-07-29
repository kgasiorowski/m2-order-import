import csv as py_csv
from pprint import pprint
from src.model.Order import Order

def generateOrdersFromCsv(filename: str) -> Order:
    with open(filename, 'r') as raw_csv_file:
        csv_reader = py_csv.DictReader(raw_csv_file)

        for line in csv_reader:
            pprint(line)