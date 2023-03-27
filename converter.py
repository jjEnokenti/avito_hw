import csv
import json


def csv_to_json(csv_path, json_path):
    data = []

    filename = csv_path.split('/')[2].split('.')[0]
    if filename == 'ads':
        model = 'ads.ad'
        field_names = ['id', 'name', 'author', 'price', 'description', 'address', 'is_published']
    else:
        model = 'ads.category'
        field_names = ['id', 'name']

    with open(csv_path, 'r', encoding='UTF-8') as file:
        cvs_reader = csv.DictReader(file, fieldnames=field_names)
        cnt = 0
        for row in cvs_reader:
            if filename == 'ads':
                if row['is_published'] == 'TRUE':
                    row['is_published'] = True
                else:
                    row['is_published'] = False

            raw_data = {'model': model, 'pk': cnt, 'fields': row}
            data.append(raw_data)
            cnt += 1

    write_json_file(data[1:], json_path)


def write_json_file(csv_data, json_path):
    with open(json_path, 'w', encoding='UTF-8') as file:
        json_string = json.dumps(csv_data, indent=4, ensure_ascii=False)
        file.write(json_string)


if __name__ == '__main__':
    csv_to_json('./fixtures/ads.csv', './fixtures/ads.json')
    csv_to_json('./fixtures/categories.csv', './fixtures/categories.json')
