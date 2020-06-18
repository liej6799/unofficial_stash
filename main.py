# Main Entry of the application.
import click
from module.login_module import login_module, validate_2fa_module, login_creds_module
from module.main_module import dashboard_module, etf_detail_module
from module.helpers.database import start_database, create_table
from module.display_module import  display_all_module
@click.group()
def cli():
    pass


@click.command()
@click.option('--email', prompt='Email',
              help='The email of your account.')
@click.option('--password', prompt=True, hide_input=True)
def login(email, password):
    """- Perform login operation with credentials"""
    login_module(email, password)


@click.command()
@click.option('--secret', prompt='Code from SMS',
              help='The code sent to your mobile device')
def validate_2fa(secret):
    """- Perform 2FA from sms"""
    validate_2fa_module(secret)


@click.command()
def login_creds():
    """- Perform login operation with env creds"""
    login_creds_module()

@click.command()
def daily():
    """- Run this task daily to update overall and securities data."""
    dashboard_module()
    etf_detail_module()


@click.command()
def display_all():
    """- Display all data"""
    display_all_module()


cli.add_command(login)
cli.add_command(login_creds)
cli.add_command(validate_2fa)
cli.add_command(daily)
cli.add_command(display_all)

if __name__ == '__main__':
    start_database()
    create_table()
    cli()