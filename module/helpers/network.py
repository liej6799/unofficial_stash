import requests
from ..helpers.json import read_file
from ..common.common_config import get_secret_base_path
from ..helpers.language import load_language

import click

headers = {'Content-Type': 'application/json;charset=utf-8',
           'x-client-identifier': 'webapp@2.29.0'}


def post_data(path, data):
    r = requests.post(path, headers=headers, data=data)
    return r.json()


def post_data_with_bearer(path, data):
    creds = read_file(get_secret_base_path())
    if creds['BearerToken'] is not '':
        r = requests.post(path, headers=get_header_auth(creds['BearerToken']), data=data)
        return r.json()
    else:
        # this is where bearer not exists
        click.echo(click.style(load_language().t('lang.BEARER_NOT_EXISTS'), fg='red'))
        return None


def get_header_auth(bearer):
    return {'Content-Type': 'application/json;charset=utf-8',
            'x-client-identifier': 'webapp@2.29.0',
            'Authorization': 'Bearer ' + bearer}
