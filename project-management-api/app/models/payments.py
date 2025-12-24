from datetime import datetime

from app.models.base import FinanceBaseModel
from app.util.const import PaymentStatus, PaymentType
from app.util.enum_field import EnumField
from app.models.apps import Apps
from peewee import *


class Payments(FinanceBaseModel):
    id = AutoField(primary_key=True)
    amount = DecimalField(max_digits=5, decimal_places=3, default=0)
    payment_type = EnumField(PaymentType)
    comment = TextField(null=True)
    status = EnumField(PaymentStatus, default=PaymentStatus.NONE)
    created_at = DateTimeField(default=datetime.now)
    app = ForeignKeyField(Apps, backref="payments", column_name="app_id")

    class Meta:
        table_name = "payments"
