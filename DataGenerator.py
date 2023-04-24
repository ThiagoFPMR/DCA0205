from abc import ABC


class DataGenerator(ABC):
    def __init__(self, file):
        pass

    def __iter__(self):
        pass


import json


class jsonDataGenerator(DataGenerator):
    def __init__(self, file):
        super().__init__(file)
        self.json_file = file

    def __iter__(self) -> dict:
        data = json.load(self.json_file)["results"]
        for row in data:
            yield row
