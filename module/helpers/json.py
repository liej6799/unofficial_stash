import json
from pathlib import Path
from ..common.common_config import get_secret_base_path
from ..models.creds_model import creds_model

def read_file(path):
    with open(path, 'r') as file:
        obj = json.loads(file.read())
        return obj


def write_file(path, data):
    with open(path, 'w') as json_file:
        json.dump(data.__dict__, json_file)


def dumps_class_to_str(input):
    return json.dumps(input.__dict__)

def check_creds_exists():
    try:
        my_abs_path = Path(get_secret_base_path()).resolve(strict=True)
    except FileNotFoundError:
        open(Path(get_secret_base_path()), "w")
        write_file(get_secret_base_path(), creds_model())
    # doesn't exist




