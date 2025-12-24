from peewee import *

from app.models.projects import Projects
from app.models.apps import Apps
from app.models.tasks import Tasks
from app.models.release import Release
from app.util.exceptions import ProjectException, AppException, TaskException
from app.dto.apps import AppDTO, ProjectDTO, TaskDTO
from app.util.generate_references import  generate_app_code, generate_unique_project_ref, generate_unique_task_ref

def get_app_by_id(app_id: int) -> Apps | None:
    app = Apps.get(Apps.id == app_id)
    if not app:
        return AppException("App not found")
    return app

def get_projects_by_app_id(app_id: int) -> list[Projects]:
    projects = Projects.select().where(Projects.app.id == app_id)
    if not projects:
        return ProjectException("No projects found for this app")
    return projects

def get_project_by_id(project_ref: str) -> Projects | None:
    project = Projects.get(Projects.project_ref == project_ref)
    if not project:
        return ProjectException("Project not found")
    return project

def get_apps(user_id: int) -> list[Apps]:
    apps = Apps.select().where(Apps.user_id == user_id)
    if not apps:
        return AppException("No apps found for this user")
    return apps

def change_status(new_status: str, task_id: int) -> Tasks:
    task = Tasks.get(Tasks.id == task_id)
    if not task:
        raise TaskException("Task not found")
    task.status = new_status
    return task

def add_task_to_project(task: TaskDTO) -> None:
    task.task_ref = generate_unique_task_ref(task.name)
    Tasks.create(**task.model_dump())

def create_project(project: ProjectDTO) -> None:
    app = Apps.get(Apps.id == project.app_id)
    project.project_ref = generate_unique_project_ref(app.name)
    Projects.create(**project.model_dump())
    
def create_app(app: AppDTO) -> None:
    app.code_name = generate_app_code(app.name)
    Apps.create(**app.model_dump())

def create_task(task: TaskDTO) -> None:
    task.task_ref = generate_unique_task_ref(task.name)
    Tasks.create(**task.model_dump())

def remove_task(task_id: int) -> None:
    task = Tasks.get(Tasks.id == task_id)
    if not task:
        raise TaskException("Task not found")
    task.delete_instance()

def remove_project(project_id: int) -> None:
    project = Projects.get(Projects.id == project_id)
    if not project:
        raise ProjectException("Project not found")
    project.delete_instance()

def remove_app(app_id: int) -> None:
    app = Apps.get(Apps.id == app_id)
    if not app:
        raise AppException("App not found")
    app.delete_instance()

def update_project(project_id: int, updated_data: ProjectDTO) -> Projects:
    project = Projects.get(Projects.id == project_id)
    if not project:
        raise ProjectException("Project not found")
    project.update(**updated_data.model_dump()).where(Projects.id == project_id).execute()
    return project

def update_task(task_id: int, updated_data: TaskDTO) -> Tasks:
    task = Tasks.get(Tasks.id == task_id)
    if not task:
        raise TaskException("Task not found")
    task.update(**updated_data.model_dump()).where(Tasks.id == task_id).execute()
    return task

def get_backlog_tasks(project_id: int) -> list[Tasks]:
    tasks = Tasks.select().where((Tasks.project_id == project_id) & (Tasks.release.is_null(True)))
    if not tasks:
        raise TaskException("No backlog tasks found for this project")
    return tasks

def get_scheduled_tasks(project_id: int, release_id: int) -> list[Tasks]:
    tasks = Tasks.select().where((Tasks.project_id == project_id) & (Tasks.release == release_id))
    if not tasks:
        raise TaskException("No scheduled tasks found for this project and release")
    return tasks

def assign_to_release(task_id: int, release_id: int) -> Tasks:
    task = Tasks.get(Tasks.id == task_id)
    if not task:
        raise TaskException("Task not found")
    release = Release.get(Release.id == release_id)
    task.release = release
    task.save()
    return task