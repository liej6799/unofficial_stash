from .common.common_config import get_json_base_path, get_environment_base_path
from .helpers.json import read_file, dumps_class_to_str
from .helpers.network import post_data
from .models.login_model import login_model
from dotenv import load_dotenv

import os

load_dotenv(dotenv_path=get_environment_base_path())


def login_with_creds(email, password):
    url = read_file(get_json_base_path())['URL_LOGIN']
    data = dumps_class_to_str(login_model(email, password))

    print(post_data(url, data))


def login_with_env():
    email = os.getenv("EMAIL")
    password = os.getenv("PASSWORD")

    if email is None or password is None:
        return "No Environment Variable set, Please create .env in /module/common/.env, add both EMAIL_STASH and " \
               "PASSWORD_STASH "

    url = read_file(get_json_base_path())['URL_LOGIN']
    data = dumps_class_to_str(login_model(email, password))

    print(post_data(url, data))
