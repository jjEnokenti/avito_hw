import csv
import json


def csv_to_json(csv_path, json_path):
    fieldnames = [
        'id',
        'name',
        'author',
        'price',
        'description',
        'address',
        'is_published'
    ]

    data = []

    with open(csv_path, 'r', encoding='UTF-8') as file:
        cvs_reader = csv.DictReader(file, fieldnames=fieldnames)

        for row in cvs_reader:
            if row['is_published']:
                row['is_published'] = row['is_published'].lower()
            data.append(row)

    write_json_file(data[1:], json_path)


def write_json_file(csv_data, json_path):
    with open(json_path, 'w', encoding='UTF-8') as file:
        json_string = json.dumps(csv_data, indent=4, ensure_ascii=False)
        file.write(json_string)


if __name__ == '__main__':
    csv_to_json('./fixtures/ads.csv', './fixtures/ads.json')
    csv_to_json('./fixtures/categories.csv', './fixtures/categories.json')
