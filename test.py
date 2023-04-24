from DataGenerator import csvDataGenerator, jsonDataGenerator

csv_path = "cafes.csv"
json_path = "cafes.json"

count = 0
for row in csvDataGenerator(csv_path):
    if float(row["rating"]) > 4:
        count += 1
print(count)

print("---------")

count = 0
for row in jsonDataGenerator(json_path):
    if float(row["rating"]) > 4:
        count += 1
print(count)
