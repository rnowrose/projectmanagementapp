from datetime import datetime
from decimal import Decimal

from app.models.base import FinanceBaseModel
from peewee import *
from app.models.categories import Categories
from app.models.apps import Apps


class Expenses(FinanceBaseModel):
    id = AutoField(primary_key=True)
    name = CharField(max_length=255, unique=True, null=False)
    description = TextField()  # TEXT field equivalent
    amount = DecimalField(max_digits=10, decimal_places=2)  # DECIMAL(10,2)
    created_at = DateTimeField(default=datetime.now)
    categories = ForeignKeyField(
        Categories, backref="expenses", column_name="category_id"
    )
    app = ForeignKeyField(
        Apps, backref="expenses", column_name="app_id"
    )  # Foreign key to Apps

    class Meta:
        table_name = "expenses"

    def save(self, *args, **kwargs):
        """Override save to ensure proper decimal handling"""
        # Ensure amount is a Decimal
        if self.amount and not isinstance(self.amount, Decimal):
            self.amount = Decimal(str(self.amount))

        return super().save(*args, **kwargs)

    @classmethod
    def create(cls, **query):
        """Override create to handle decimal conversion"""
        if "amount" in query and not isinstance(query["amount"], Decimal):
            query["amount"] = Decimal(str(query["amount"]))
        return super().create(**query)

    def __str__(self):
        return f"{self.name}: ${self.amount}"

    @property
    def formatted_amount(self):
        """Get formatted amount as string"""
        return f"${self.amount:.2f}"
