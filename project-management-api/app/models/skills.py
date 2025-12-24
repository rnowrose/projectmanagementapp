from peewee import *
from app.models.base import UserBaseModel
from app.util.const import ProficiencyLevel
from app.util.enum_field import EnumField
from app.models.users import Users

class Skills(UserBaseModel):
    id = AutoField(primary_key=True)
    name = CharField(max_length=255, unique=True, index=True, null=False)
    description = TextField(null=True)
    proficiency_level = EnumField(enum_class=ProficiencyLevel, null=False)
    user = ForeignKeyField(
        Users, backref="skills", null=True
    )
    
    class Meta:
        table_name = 'skills'