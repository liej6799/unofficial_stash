from datetime import date
import click
from .models.database_model import Goals, Securities
from tabulate import tabulate
from .helpers.language import load_language
import os


def display_all_module():

    os.system("cls")

    select_date = date.today()
    select_goals = Goals.select().where(Goals.created_date == select_date)
    select_securities = Securities.select().where(Securities.created_date == select_date)
    click.echo('\n')
    click.echo(click.style(
        load_language().t('lang.DISPLAY_HEADER_OVERVIEW', date=select_date)))
    click.echo('\n')

    all_name = []
    all_currency = []
    all_amount = []
    all_daily_amount_changes = []

    net_amount = 0
    for element in select_goals:
        all_name.append(element.name)
        all_currency.append(element.currency)
        all_amount.append(element.amount)
        all_daily_amount_changes.append(element.daily_amount_changes)
        net_amount = net_amount + element.amount

    goals_headers = ['Name', 'Currency', 'Amount', 'Daily Changes']
    goals_table = zip(all_name, all_currency, all_amount, all_daily_amount_changes)



    all_symbol = []
    all_units = []
    all_price = []
    all_value = []

    all_daily_units_changes = []
    all_daily_price_changes = []
    all_daily_value_changes = []


    for element in select_securities:
        all_symbol.append(element.symbol)
        all_units.append(element.units)
        all_price.append(element.price)
        all_value.append(element.value)

        all_daily_units_changes.append(element.daily_units_changes)
        all_daily_price_changes.append(element.daily_price_changes)
        all_daily_value_changes.append(element.daily_value_changes)

    securities_headers = ['Symbol', 'Units', 'Price', 'Value', 'Daily Unit Changes', 'Daily Price Changes', 'Daily Value Changes']
    securities_table = zip(all_symbol, all_units, all_price, all_value, all_daily_units_changes, all_daily_price_changes, all_daily_value_changes)





    print(tabulate(goals_table, tablefmt="github", headers=goals_headers))

    click.echo('\n')
    total = zip(['Total'], [all_currency[0]], [net_amount])
    print(tabulate(total, tablefmt="github"))
    click.echo('\n')
    print(tabulate(securities_table, tablefmt="github", headers=securities_headers))
