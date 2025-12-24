from peewee import *
from playhouse.postgres_ext import BinaryJSONField
from datetime import datetime
from app.models.base import ProjectManagementBaseModel


class Release(ProjectManagementBaseModel):
    id = AutoField(primary_key=True)
    name = CharField(max_length=255, unique=True, null=False)
    version = CharField(max_length=50, unique=True, null=False)
    description = TextField()
    release_date = DateTimeField(null=False)
    created_at = DateTimeField(default=datetime.now)
    updated_at = DateTimeField(default=datetime.now)
    tasks = BinaryJSONField()  
    
    class Meta:
        table_name = 'releases'
    
    