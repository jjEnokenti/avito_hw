import csv
import json


def csv_to_json(csv_path, json_path, model):
    data = []

    with open(csv_path, 'r', encoding='UTF-8') as file:
        cvs_reader = csv.DictReader(file)

        for row in cvs_reader:
            raw_data = {'model':  model, 'pk': int(row['id'] if 'id' in row else row['Id'])}

            if 'id' in row:
                del row['id']
            else:
                del row['Id']

            if 'is_published' in row:
                if row['is_published'] == 'TRUE':
                    row['is_published'] = True
                else:
                    row['is_published'] = False

            raw_data['fields'] = row
            data.append(raw_data)

    write_json_file(data, json_path)


def write_json_file(csv_data, json_path):
    with open(json_path, 'w', encoding='UTF-8') as file:
        json_string = json.dumps(csv_data, indent=4, ensure_ascii=False)
        file.write(json_string)


if __name__ == '__main__':
    csv_to_json('./fixtures/ads.csv', './fixtures/ads.json', 'ads.ad')
    csv_to_json('./fixtures/categories.csv', './fixtures/categories.json', 'ads.category')
