from datetime import datetime

from app.models.base import ProjectManagementBaseModel
from app.util.const import PriorityLevel, TaskStatus
from app.util.enum_field import EnumField
from app.models.projects import Projects
from app.models.release import Release
from peewee import *


class Tasks(ProjectManagementBaseModel):
    id = AutoField(primary_key=True)
    task_ref=CharField(max_length=100, unique=True, null=False)
    name = CharField(max_length=255, unique=True, null=False)
    type = CharField(max_length=100, null=False)
    points = IntegerField(null=False)
    story = TextField()  # TEXT field equivalent
    status = EnumField(TaskStatus, null=True)
    priority = EnumField(PriorityLevel, null=True)
    created_at = DateTimeField(default=datetime.now)
    updated_at = DateTimeField(default=datetime.now)
    github_url = CharField(max_length=500, null=True)
    project = ForeignKeyField(Projects, backref="tasks", column_name="project_id")
    release = ForeignKeyField(Release, backref="tasks", column_name="release_id", null=True)
    class Meta:
        table_name = "tasks"

    @property
    def is_in_backlog(self):
        return self.release is None
    
    @property
    def is_scheduled(self):
        return self.release is not None

    @property
    def is_completed(self):
        return self.status_enum == TaskStatus.COMPLETED if self.status_enum else False

    def __str__(self):
        return f"{self.name} ({self.status or 'Unknown'}) - {self.days} days"
