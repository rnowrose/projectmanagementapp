from peewee import *
from app.models.base import UserBaseModel
from app.models.users import Users


class Education(UserBaseModel):
    id = AutoField(primary_key=True)
    degree = CharField(max_length=255)
    institution = CharField(max_length=255)
    location = CharField(max_length=100, null=True)
    start_date = DateField()
    end_date = DateField(null=True)
    description = TextField()
    user = ForeignKeyField(
        Users, backref="education", null=True
    )
    
    class Meta:
        table_name = 'education'
