import json


def read_file(path):
    with open(path, 'r') as file:
        obj = json.loads(file.read())
        return obj


def write_file(path, data):
    with open(path, 'w') as json_file:
        json.dump(data.__dict__, json_file)


def dumps_class_to_str(input):
    return json.dumps(input.__dict__)
