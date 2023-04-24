from abc import ABC


class DataGenerator(ABC):
    def __init__(self, páth):
        pass

    def __iter__(self):
        pass


import csv  # adaptee


class csvDataGenerator(DataGenerator):
    def __init__(self, path):
        super().__init__(path)
        self.csv_path = path

    def __iter__(self) -> dict:
        with open(self.csv_path, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                yield row


import json  # adaptee


class jsonDataGenerator(DataGenerator):
    def __init__(self, path):
        super().__init__(path)
        self.json_path = path

    def __iter__(self) -> dict:
        with open(self.json_path, "r") as f:
            data = json.load(f)["results"]
            for row in data:
                yield row
