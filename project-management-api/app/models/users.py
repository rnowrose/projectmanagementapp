from peewee import *
from datetime import datetime
from passlib.context import CryptContext
from app.models.base import UserBaseModel
import bcrypt



class Users(UserBaseModel):
    id = AutoField(primary_key=True)
    first_name = CharField(max_length=255, null=True)
    last_name = CharField(max_length=255, null=False)
    email = CharField(max_length=255, unique=True, index=True, null=False)
    phone_number = CharField(max_length=20, null=True)
    username = CharField(max_length=255, unique=True, index=True, null=False)
    hashed_password = CharField(max_length=255, null=False)
    is_active = BooleanField(default=True)
    created_at = DateTimeField(default=datetime.now) 
    token = CharField(max_length=512, null=True) 
    summary = TextField(null=True)
    github_url = CharField(max_length=255, null=True)
    linkedin_url = CharField(max_length=255, null=True)
    website_url = CharField(max_length=255, null=True)
    profile_picture = CharField(max_length=512, null=True)
    updated_at = DateTimeField(default=datetime.now)
    
    class Meta:
        table_name = 'users'
    
    def verify_password(self, password: str) -> bool:
        """Verify a password against the hashed password"""
        return bcrypt.checkpw(password.encode('utf-8'), self.hashed_password.encode('utf-8'))
    
    @classmethod
    def hash_password(cls, password: str) -> str:
        """Hash a password for storing in database"""
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
    @classmethod
    def authenticate(cls, username: str, password: str) -> bool:
        """Authenticate user by username and password"""
        try:
            user = cls.get(cls.username == username)
            if user.verify_password(password) and user.is_active:
                return True
        except cls.DoesNotExist:
            pass
        return False
    
    @property
    def full_name(self):
        """Get user's full name"""
        if self.first_name:
            return f"{self.first_name} {self.last_name}"
        return self.last_name
    
    def __str__(self):
        return f"{self.username} ({self.full_name})"