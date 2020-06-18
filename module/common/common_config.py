import pathlib


def get_json_base_path():
    return str(pathlib.Path(__file__).parent.absolute()) + "/urls.json"

def get_api_status_base_path():
    return str(pathlib.Path(__file__).parent.absolute()) + "/api_status.json"

def get_language_base_path():
    return str(pathlib.Path(__file__).parent.absolute()) + "/languages"

def get_secret_base_path():
    return str(pathlib.Path(__file__).parent.absolute()) + "/creds.json"

