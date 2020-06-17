from ..models.database_model import *


def start_database():
    db.connect()


def create_table():
    db.create_tables([Goals])
    db.create_tables([Securities])
