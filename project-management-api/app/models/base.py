from peewee import Model
from app.db.database import db

class BaseModel(Model):
    class Meta:
        database = db

class UserBaseModel(BaseModel):
    class Meta:
        schema = 'users'

class ProjectManagementBaseModel(BaseModel):
    class Meta:
        schema = 'project_management'
        
class FinanceBaseModel(BaseModel):
    class Meta:
        schema = 'finance'