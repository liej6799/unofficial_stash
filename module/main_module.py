from .common.common_config import get_json_base_path, get_secret_base_path, get_api_status_base_path
from .helpers.json import read_file, dumps_class_to_str, write_file
from .helpers.network import post_data, post_data_with_bearer
from .models.main_model import dashboard_model
from .models.database_model import db, Goals

from datetime import date, timedelta

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
            try:
                latest_goals_date = Goals.select()[-1].created_date
            except IndexError:
                latest_goals_date = date.today() - timedelta(days=1)
            dashboard_goals = dashboard_result['data']['goals']
            if (date.today() > latest_goals_date):
                if len(dashboard_goals) > 0:
                    daily_amount_changes = 0
                    for element in dashboard_goals:
                        for goals in Goals.select().where(Goals.created_date == latest_goals_date):
                            if (goals.goals_id == element['_id']):
                                daily_amount_changes = element['portfolioPerformance']['currentNav'] - goals.amount

                        goals = Goals(goals_id=element['_id'], name=element['displayName'],
                                      currency=element['portfolioPerformance']['currency'],
                                      amount=element['portfolioPerformance']['currentNav'],
                                      daily_amount_changes=daily_amount_changes)
                        goals.save()

                        for goals in Goals.select().where(Goals.created_date == date.today()):
                            print_dashboard(goals.name, goals.goals_id, goals.currency, goals.amount,
                                            goals.daily_amount_changes)
            else:
                # Instead of read new data, read previous one
                for goals in Goals.select().where(Goals.created_date == date.today()):
                    print_dashboard(goals.name, goals.goals_id, goals.currency, goals.amount,
                                    goals.daily_amount_changes)


        except KeyError:
            click.echo(dashboard_result)
        except TypeError:
            dashboard_error = dashboard_result['errors'][0]['id']
            if dashboard_error == api_status['VALIDATE2FA_INVALID']['id']:
                click.echo(click.style(load_language().t('lang.BEARER_EXPIRED'), fg='red'))


def print_dashboard(name, goals_id, currency, amount, daily_amount_changes):
    color = 'green';
    if daily_amount_changes < 0:
        color = 'red'
    elif daily_amount_changes == 0:
        color = 'black'

    click.echo(click.style(name + ' - ' + goals_id))
    click.echo(currency + ' ' + str(amount) + ' ' + click.style(str(daily_amount_changes), fg=color))
