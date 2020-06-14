from .common.common_config import get_json_base_path, get_secret_base_path, get_api_status_base_path
from .helpers.json import read_file, dumps_class_to_str, write_file
from .helpers.network import post_data, post_data_with_bearer
from .models.main_model import dashboard_model

from .helpers.language import load_language
import click

api_status = read_file(get_api_status_base_path())
url_dashboard = read_file(get_json_base_path())['URL_DASHBOARD']


def dashboard_module():
    dashboard_input = dumps_class_to_str(dashboard_model())
    dashboard_result = post_data_with_bearer(url_dashboard, dashboard_input)
    # try get the goals first
    if dashboard_result is not None:
        try:
            dashboard_goals = dashboard_result['data']['goals']
            if len(dashboard_goals) > 0:
                for element in dashboard_goals:
                    click.echo(click.style(element['displayName'] + ' - ' + element['_id'], fg='green'))
                    click.echo(click.style(element['portfolioPerformance']['currency'] + ' ' + str(
                        element['portfolioPerformance']['currentNav']), fg='green'))
        except KeyError:
            click.echo(dashboard_result)
        except TypeError:
            dashboard_error = dashboard_result['errors'][0]['id']
            if dashboard_error == api_status['VALIDATE2FA_INVALID']['id']:
                click.echo(click.style(load_language().t('lang.BEARER_EXPIRED'), fg='red'))
