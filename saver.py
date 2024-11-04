import csv
import json

with open('itemsData.txt', 'r') as file:
    data = json.loads(file.read())


with open('itemsData.txt', 'w', encoding='utf-8', newline='') as fileCSV:
    wr = csv.DictWriter(fileCSV, fieldnames=data[0].keys)
    wr.writeheader()
    wr.writerows(data)
