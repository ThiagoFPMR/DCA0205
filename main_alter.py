import csv


def main_csv(path):
    count = 0
    with open(path, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if float(row["rating"]) > 4:
                count += 1
    return count


import json


def main_json(path):
    count = 0
    with open(path, "r") as f:
        data = json.load(f)["results"]
        for row in data:
            if float(row["rating"]) > 4:
                count += 1
    return count


csv_path, json_path = "cafes.csv", "cafes.json"


print("out usando csv:", main_csv(csv_path))
print("--------------------")
print("out usando json:", main_json(json_path))
