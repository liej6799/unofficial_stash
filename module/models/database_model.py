from peewee import *
from datetime import date
from playhouse.migrate import *

db = SqliteDatabase('unofficial_stash.db')
migrator = SqliteMigrator(db)


class BaseModel(Model):
    class Meta:
        database = db


class Goals(BaseModel):
    goals_id = IntegerField()
    name = CharField()
    currency = CharField()
    amount = FloatField()
    created_date = DateField(default=date.today(), null=True)

    daily_amount_changes = FloatField()


class Securities(BaseModel):
    symbol = CharField()
    units = FloatField()
    price = FloatField()
    value = FloatField()
    created_date = DateField(default=date.today(), null=True)

    daily_units_changes = FloatField()
    daily_price_changes = FloatField()
    daily_value_changes = FloatField()
