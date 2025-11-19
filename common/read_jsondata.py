import json


def read_json(filename):
    list_data = []
    with open(filename, encoding="utf-8") as f:
        json_data = json.load(f)
        for i in json_data:
            list_data.append(tuple(i.values()))
        return list_data


