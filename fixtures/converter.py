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

            if 'age' in row:
                row['age'] = int(row['age'])

            if 'location_id' in row:
                row['location_id'] = int(row['location_id'])

            if 'price' in row:
                row['price'] = int(row['price'])

            if 'author_id' in row:
                row['author_id'] = int(row['author_id'])
            if 'category_id' in row:
                row['category_id'] = int(row['category_id'])

            if 'lat' in row:
                row['lat'] = float(row['lat'])
            if 'lng' in row:
                row['lng'] = float(row['lng'])

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
    csv_to_json('./fixtures/ad.csv', './fixtures/ad.json', 'ads.ad')
    csv_to_json('./fixtures/category.csv', './fixtures/category.json', 'ads.category')
    csv_to_json('./fixtures/location.csv', './fixtures/location.json', 'ads.location')
    csv_to_json('./fixtures/user.csv', './fixtures/user.json', 'ads.user')
