from app.models.base import UserBaseModel
from app.util.const import WorkType
from app.util.enum_field import EnumField
from peewee import *
from app.models.users import Users


class Experiences(UserBaseModel):
    id = AutoField(primary_key=True)
    company_name = CharField(max_length=255, unique=True, null=False)
    location = CharField(max_length=255, null=True)
    work_type = EnumField(WorkType)  # Store enum as string
    start_date = DateTimeField(null=False)
    end_date = DateTimeField(null=False)
    description = TextField()  # Equivalent to TEXT column
    user = ForeignKeyField(Users, backref="experiences", column_name="user_id")

    class Meta:
        table_name = "experiences"
