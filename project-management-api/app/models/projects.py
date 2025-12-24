from datetime import datetime

from app.models.base import ProjectManagementBaseModel
from app.models.apps import Apps
from peewee import *


class Projects(ProjectManagementBaseModel):
    id = AutoField(primary_key=True)
    project_ref=CharField(max_length=100, unique=True, null=False)
    name = CharField(max_length=255, unique=True, null=False)
    start_date = DateTimeField(null=False)
    end_date = DateTimeField(null=False)
    timestamp = DateTimeField(null=False)
    description = TextField()
    created_at = DateTimeField(default=datetime.now)
    updated_at = DateTimeField(default=datetime.now)
    app = ForeignKeyField(Apps, backref="projects", column_name="app_id")

    class Meta:
        table_name = "projects"

    def save(self, *args, **kwargs):
        """Override save to update timestamp"""
        self.updated_at = datetime.now()
        return super().save(*args, **kwargs)

    @property
    def duration_days(self):
        """Calculate project duration in days"""
        if self.start_date and self.end_date:
            return (self.end_date - self.start_date).days
        return 0

    @property
    def is_active(self):
        """Check if project is currently active"""
        now = datetime.now()
        return self.start_date <= now <= self.end_date

    def __str__(self):
        return f"{self.name} ({self.release or 'No release'})"
