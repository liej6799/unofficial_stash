# Main Entry of the application. 

import click
import os
from module.login_module import login_with_creds, login_with_env


@click.group()
def cli():
    pass


@click.command()
@click.option('--email', prompt='Email',
              help='The email of your account.')
@click.option('--password', prompt=True, hide_input=True)
def logincreds(email, password):
    """- Perform login operation with credentials"""
    login_with_creds(email, password)

@click.command()
def loginenv():
    """- Perform login operation with environment variable."""
    click.echo(login_with_env())


cli.add_command(logincreds)
cli.add_command(loginenv)

if __name__ == '__main__':
    cli()
