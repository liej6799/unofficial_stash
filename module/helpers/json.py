import json


def read_file(path):
    with open(path, 'r') as file:
        obj = json.loads(file.read())
        return obj


def dumps_class_to_str(input):
    return json.dumps(input.__dict__)
