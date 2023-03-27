import csv
import json


def csv_to_json(csv_path, json_path):
    data = []

    with open(csv_path, 'r', encoding='UTF-8') as file:
        cvs_reader = csv.DictReader(file)

        for row in cvs_reader:
            data.append(row)

    write_json_file(data, json_path)


def write_json_file(csv_data, json_path):
    with open(json_path, 'w', encoding='UTF-8') as file:
        json_string = json.dumps(csv_data, indent=4, ensure_ascii=False)
        file.write(json_string)


if __name__ == '__main__':
    csv_to_json('./fixtures/ads.csv', './fixtures/ads.json')
    csv_to_json('./fixtures/categories.csv', './fixtures/categories.json')
