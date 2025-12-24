from peewee import *
from app.models.base import FinanceBaseModel
from app.util.const import CategoryType
from app.util.enum_field import EnumField

class Categories(FinanceBaseModel):
    id = AutoField(primary_key=True)
    name = CharField(max_length=255, unique=True, null=False)
    description = TextField(null=True)
    type = EnumField(CategoryType, null=False)
    
    class Meta:
        table_name = 'categories'