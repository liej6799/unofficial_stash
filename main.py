# Main Entry of the application. 

import click
import os
from module.login_module import login_module, validate_2fa_module


@click.group()
def cli():
    pass


@click.command()
@click.option('--email', prompt='Email',
              help='The email of your account.')
@click.option('--password', prompt=True, hide_input=True)
def login(email, password):
    """- Perform login operation with credentials"""
    login_module(email, password);


@click.command()
@click.option('--secret', prompt='Code from SMS',
              help='The code sent to your mobile device')
def validate_2fa(secret):
    """- Perform 2FA from sms"""

    validate_2fa_module(secret);


cli.add_command(login)
cli.add_command(validate_2fa)

if __name__ == '__main__':
    cli()
