from peewee import *
from datetime import datetime
from app.models.base import ProjectManagementBaseModel
from app.models.users import Users



class Clients(ProjectManagementBaseModel):
    id = AutoField(primary_key=True)
    name = CharField(max_length=255, unique=True, null=False)
    contact_email = CharField(max_length=255, null=False)
    phone_number = CharField(max_length=20, null=True)
    address = TextField(null=True)
    created_at = DateTimeField(default=datetime.now)
    updated_at = DateTimeField(default=datetime.now)
    user = ForeignKeyField(
        Users, backref="clients", column_name="user_id", null=True)
    
    class Meta:
        table_name = 'clients'
    
    def save(self, *args, **kwargs):
        """Override save to update timestamp"""
        self.updated_at = datetime.now()
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.name} ({self.contact_email})"