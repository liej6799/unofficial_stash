import pathlib


def get_json_base_path():
    return str(pathlib.Path(__file__).parent.absolute()) + "\\urls.json"

def get_environment_base_path():
    return str(pathlib.Path(__file__).parent.absolute()) + "\\.env"

