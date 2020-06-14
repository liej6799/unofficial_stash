from .common.common_config import get_json_base_path, get_secret_base_path, get_api_status_base_path
from .helpers.json import read_file, dumps_class_to_str, write_file
from .helpers.network import post_data
from .models.login_model import login_model, login_2fa_send_model, validate_2fa_model
from .models.creds_model import creds_model

from .helpers.language import load_language
import click

api_status = read_file(get_api_status_base_path())
url = read_file(get_json_base_path())['URL_LOGIN']
url_2fa_send = read_file(get_json_base_path())['URL_2FA_SEND']
url_2fa = read_file(get_json_base_path())['URL_2FA']


def login_module(email, password):
    cred = dumps_class_to_str(login_model(email, password))
    login_result = post_data(url, cred)

    try:
        login_id = login_result['id']
        login_error = ''
    except KeyError:
        login_error = login_result['message']
        login_id = ''

    if login_error == api_status['LOGIN_EMAIL_NOT_VALID']['messages']:
        click.echo(click.style(load_language().t('lang.LOGIN_EMAIL_NOT_VALID'), fg='red'))

    elif login_id == api_status['LOGIN_PASSWORD_NOT_VALID']['id']:
        click.echo(click.style(load_language().t('lang.LOGIN_PASSWORD_NOT_VALID'), fg='red'))

    elif login_id == api_status['LOGIN_SUCCESS_2FA']['id']:
        token = login_result['token']
        token_input = dumps_class_to_str(login_2fa_send_model(email, token))

        token_result = post_data(url_2fa_send, token_input)
        try:
            token_id = token_result['id']
            smsSent = False
        except KeyError:
            token_id = ''
            smsSent = token_result['smsSent']

        if smsSent is True:

            creds = read_file(get_secret_base_path())
            write_file(get_secret_base_path(), creds_model(creds['BearerToken'], creds['UserId'], token, email, password))

            click.echo(click.style(
                load_language().t('lang.LOGIN_SUCCESS_2FA_HEAD', number=token_result['smsNumber']),
                fg='green'))

            click.echo(click.style(load_language().t('lang.LOGIN_SUCCESS_2FA_END')))

        elif token_id == api_status['LOGIN_SUCCESS_2FA_LOCKED']['id']:
            click.echo(click.style(load_language().t('lang.LOGIN_SUCCESS_2FA_LOCKED'), fg='red'))


def validate_2fa_module(secret):
    validate_2fa_input = dumps_class_to_str(validate_2fa_model(read_file(get_secret_base_path())['OtpToken'], secret))
    validate_2fa_result = post_data(url_2fa, validate_2fa_input)
    print(validate_2fa_result)
    try:
        validate_2fa_token_id = validate_2fa_result['id']
        validate_2fa_user_id = ''
        validate_2fa_token = ''
    except KeyError:
        validate_2fa_token_id = ''
        validate_2fa_user_id = validate_2fa_result['userId']
        validate_2fa_token = validate_2fa_result['token']

    if validate_2fa_token_id == api_status['VALIDATE2FA_INVALID']['id']:
        click.echo(click.style(load_language().t('lang.VALIDATE2FA_INVALID'), fg='red'))
    # assume login success
    # save the data to env
    else:
        click.echo(click.style(load_language().t('lang.VALIDATE2FA_SUCCESS'), fg='green'))
        creds = read_file(get_secret_base_path())
        write_file(get_secret_base_path(), creds_model(validate_2fa_token, validate_2fa_user_id, "", creds['Email'], creds['Password']))


def login_creds_module():
    creds = read_file(get_secret_base_path())
    if creds['Email'] != '' and creds['Password'] != '':
        login_module(creds['Email'], creds['Password'])

    else:
        click.echo(click.style(load_language().t('lang.AUTO_LOGIN_NOT_EXISTS'), fg='red'))
