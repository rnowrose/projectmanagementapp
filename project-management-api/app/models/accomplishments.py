from peewee import *
from datetime import datetime
from app.models.base import UserBaseModel
from app.models.users import Users
from app.util.enum_field import EnumField
from app.util.const import AccomplishmentType

class Accomplishment(UserBaseModel):
    id = AutoField()
    user = ForeignKeyField(Users, backref='accomplishments')
    title = CharField(max_length=255)
    description = TextField()
    date_achieved = DateField()
    accomplishment_type = EnumField(AccomplishmentType) # e.g., 'Award', 'Certification', 'Project'
    
    
    class Meta:
        table_name = 'accomplishments'