from .common.common_config import get_json_base_path, get_secret_base_path, get_api_status_base_path
from .helpers.json import read_file, dumps_class_to_str, write_file
from .helpers.network import post_data, post_data_with_bearer
from .models.main_model import dashboard_model, asset_performance_model, etf_detail_model, securities_model
from .models.database_model import db, Goals, Securities

from datetime import date, timedelta
from collections import OrderedDict

from .helpers.language import load_language
import click

api_status = read_file(get_api_status_base_path())
url_dashboard = read_file(get_json_base_path())['URL_DASHBOARD']
url_asset_performance = read_file(get_json_base_path())['URL_ASSET_PERFORMANCE']
url_etf_detail_model = read_file(get_json_base_path())['URL_ETF_DETAIL']


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
            if date.today() > latest_goals_date:
                if len(dashboard_goals) > 0:
                    daily_amount_changes = 0
                    for element in dashboard_goals:
                        for goals in Goals.select().where(Goals.created_date == latest_goals_date):
                            if goals.goals_id == element['_id']:
                                daily_amount_changes = element['portfolioPerformance']['currentNav'] - goals.amount

                        goals = Goals(goals_id=element['_id'], name=element['displayName'],
                                      currency=element['portfolioPerformance']['currency'],
                                      amount=element['portfolioPerformance']['currentNav'],
                                      daily_amount_changes=daily_amount_changes)
                        goals.save()
                    net_amount = 0
                    net_daily_amount_changes = 0
                    currency = ''
                    for goals in Goals.select().where(Goals.created_date == date.today()):
                        print_dashboard(goals.name, goals.goals_id, goals.currency, goals.amount,
                                        goals.daily_amount_changes)
                        net_amount = net_amount + goals.amount
                        net_daily_amount_changes = net_daily_amount_changes + goals.daily_amount_changes
                        currency = goals.currencys
                    print_net(currency, net_amount, net_daily_amount_changes)
            else:
                # Instead of read new data, read previous one
                net_amount = 0
                net_daily_amount_changes = 0
                currency = ''
                for goals in Goals.select().where(Goals.created_date == date.today()):
                    print_dashboard(goals.name, goals.goals_id, goals.currency, goals.amount,
                                    goals.daily_amount_changes)
                    net_amount = net_amount + goals.amount
                    net_daily_amount_changes = net_daily_amount_changes + goals.daily_amount_changes
                    currency = goals.currency
                print_net(currency, net_amount, net_daily_amount_changes)
        except KeyError:
            click.echo(dashboard_result)
        except TypeError:
            dashboard_error = dashboard_result['errors'][0]['id']
            if dashboard_error == api_status['VALIDATE2FA_INVALID']['id']:
                click.echo(click.style(load_language().t('lang.BEARER_EXPIRED'), fg='red'))


def asset_performance_module():
    securities_symbol = []
    for goals in Goals.select().where(Goals.created_date == date.today()):
        asset_performance_input = dumps_class_to_str(asset_performance_model(goals.goals_id))
        asset_performance_result = post_data_with_bearer(url_asset_performance, asset_performance_input)

        if asset_performance_result is not None:
            try:
                asset_performance_portfolio_securities = \
                asset_performance_result['data']['goal']['portfolioAssetsPerformance']['securities']
                if len(asset_performance_portfolio_securities) > 0:
                    for securities in asset_performance_portfolio_securities:
                        securities_symbol.append(securities['symbol'])
            except KeyError:
                click.echo(asset_performance_result)
            except TypeError:
                dashboard_error = asset_performance_result['errors'][0]['id']
                if dashboard_error == api_status['VALIDATE2FA_INVALID']['id']:
                    click.echo(click.style(load_language().t('lang.BEARER_EXPIRED'), fg='red'))
    print(list(OrderedDict.fromkeys(securities_symbol)))


def etf_detail_module():
    all_securities = []

    try:
        latest_securities_date = Securities.select()[-1].created_date
    except IndexError:
        latest_securities_date = date.today() - timedelta(days=1)
    if date.today() > latest_securities_date:
        for goals in Goals.select().where(Goals.created_date == date.today()):
            etf_detail_input = dumps_class_to_str(etf_detail_model(goals.goals_id))
            etf_detail_result = post_data_with_bearer(url_etf_detail_model, etf_detail_input)

            if etf_detail_result is not None:
                try:
                    asset_performance_portfolio_securities = \
                        etf_detail_result['data']['goal']['portfolioAssetsPerformance']['securities']
                    if len(asset_performance_portfolio_securities) > 0:
                        for securities in asset_performance_portfolio_securities:
                            found = False
                            for element in all_securities:
                                if element.symbol == securities['symbol']:
                                    element.units = element.units + securities['units']
                                    element.value = element.value + (element.units * element.price)
                                    found = True
                                    break

                            if not found:
                                if securities['units'] is not None:
                                    if securities['units'] != 0.0:
                                        all_securities.append(securities_model(securities['symbol'], securities['units'],
                                                             securities['lastPrice'],
                                                             securities['totalValue']))
                except KeyError:
                    click.echo(etf_detail_result)
                except TypeError:
                    dashboard_error = etf_detail_result['errors'][0]['id']
                    if dashboard_error == api_status['VALIDATE2FA_INVALID']['id']:
                        click.echo(click.style(load_language().t('lang.BEARER_EXPIRED'), fg='red'))

        daily_units_changes = 0
        daily_price_changes = 0
        daily_value_changes = 0
        print(len(all_securities))
        for x in all_securities:

            for y in Securities.select().where(Securities.created_date == latest_securities_date):
                if y.symbol == x.symbol:
                    daily_units_changes = y.units - x.units
                    daily_price_changes = y.price - x.price
                    daily_value_changes = y.value - x.value

            print(x.symbol)
            securities = Securities(symbol=x.symbol, units=x.units, price=x.price, value=x.value,
                                        daily_units_changes=daily_units_changes,
                                        daily_price_changes=daily_price_changes,
                                        daily_value_changes=daily_value_changes)
            securities.save()
    else:
        for y in Securities.select().where(Securities.created_date == date.today()):
            print_etf_detail(y.symbol, y.units, y.price, y.value)


def print_dashboard(name, goals_id, currency, amount, daily_amount_changes):
    color = 'green';
    if daily_amount_changes < 0:
        color = 'red'
    elif daily_amount_changes == 0:
        color = 'black'

    click.echo(click.style(name + ' - ' + goals_id))
    click.echo(currency + ' ' + str(amount))
    click.echo('Changes' + ' - ' + click.style(str(round(daily_amount_changes, 2)), fg=color))


def print_net(currency, net_amount, net_daily_amount_changes):
    click.echo('-----------------------------')
    click.echo('Total' + ' - ' + currency + ' ' + str(net_amount))
    click.echo('Net Daily Amount Change' + ' - ' + currency + ' ' + str(round(net_daily_amount_changes, 2)))


def print_etf_detail(symbol, units, price, value):
    click.echo(click.style(symbol + ' - ' + str(units)))
