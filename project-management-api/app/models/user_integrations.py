from peewee import *

from app.models.base import UserBaseModel
from app.models.users import Users
from app.util.const import IntegrationType
from app.util.enum_field import EnumField

class UserIntegrations(UserBaseModel):
    id = AutoField(primary_key=True)
    integration_name = CharField(max_length=255, null=False)
    integration_type = EnumField(IntegrationType, null=False)
    api_key = CharField(max_length=512, null=False)
    user = ForeignKeyField(
        Users, backref="user_integrations", null=True
    )
    
    class Meta:
        table_name = 'user_integrations'
