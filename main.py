from DataGenerator import DataGenerator, csvDataGenerator, jsonDataGenerator

csv_path, json_path = "cafes.csv", "cafes.json"


def main(dataGenerator: DataGenerator, path: str) -> int:
    count = 0
    for row in dataGenerator(path):
        if float(row["rating"]) > 4:  # establecimentos com rating maior que 4
            count += 1
    return count


print("out usando csv:", main(csvDataGenerator, csv_path))
print("--------------------")
print("out usando json:", main(jsonDataGenerator, json_path))
