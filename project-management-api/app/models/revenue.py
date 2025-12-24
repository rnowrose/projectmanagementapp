from datetime import datetime

from app.models.base import FinanceBaseModel
from app.models.categories import Categories
from app.models.payments import Payments
from peewee import *


class Revenue(FinanceBaseModel):
    id = AutoField(primary_key=True)
    name = CharField(max_length=255, null=False)
    description = TextField()
    date = DateTimeField(null=False)
    amount = DecimalField(max_digits=10, decimal_places=2)
    categories = ForeignKeyField(
        Categories, backref="revenues", column_name="category_id", null=True
    )
    payments = ForeignKeyField(
        Payments, backref="revenues", column_name="payment_id", null=True
    )
    
    class Meta:
        table_name = 'revenues'
