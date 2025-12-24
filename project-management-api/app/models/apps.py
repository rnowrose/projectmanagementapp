from datetime import datetime

from app.models.base import ProjectManagementBaseModel
from app.models.users import Users
from app.models.clients import Clients
from app.util.const import WorkType
from app.util.enum_field import EnumField
from peewee import *


class Apps(ProjectManagementBaseModel):
    id = AutoField(primary_key=True)  # Auto-incrementing primary key
    name = CharField(max_length=255, unique=True, null=False)
    code_name = CharField(max_length=100, unique=True, null=False)
    description = TextField()  # TEXT field equivalent
    created_at = DateTimeField(default=datetime.now)
    updated_at = DateTimeField(default=datetime.now)
    work_type = EnumField(WorkType, null=False)
    host = CharField(max_length=255, null=False)
    user = ForeignKeyField(
        Users, backref="apps", null=True
    )  # Foreign key to Users
    clients = ForeignKeyField(
        Clients, backref="apps", null=True
    )  # Foreign key to Clients

    class Meta:
        table_name = "apps"
        schema = "project_management"
