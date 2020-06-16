from peewee import *
from datetime import date
from playhouse.migrate import *

db = SqliteDatabase('unofficial_stash.db')
migrator = SqliteMigrator(db)

class BaseModel(Model):
    class Meta:
        database = db


class Goals(BaseModel):
    goals_id = IntegerField(default=0)
    name = CharField(default='')
    currency = CharField(default='')
    amount = FloatField(default=0)
    created_date = DateField(default=date.today(), null=True)

    daily_amount_changes = FloatField()
