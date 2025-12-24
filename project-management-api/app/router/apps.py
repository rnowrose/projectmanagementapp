from typing import List
from fastapi import APIRouter

from app.service.projects import *
from app.dto.apps import ProjectDTO
from app.dto.apps import AppDTO

router = APIRouter(prefix="/apps", tags=["apps"])

@router.get("/projects/{app_id}", response_model=List[ProjectDTO])
async def read_projects(app_id) -> List[ProjectDTO]:
    projects = get_projects_by_app_id(app_id)
    if not app_id:
        raise AppException("App not found")
    return list(projects)

@router.post("", response_model=List[AppDTO])
async def get_apps(user_id: int) -> List[AppDTO]:
   apps = get_apps(user_id)
   if not apps:
       raise AppException("No apps found for this user")
   return apps

@router.get("/app/{app_id}", response_model=AppDTO)
async def get_app(app_id: int) -> AppDTO:
    app = get_app_by_id(app_id)
    if not app:
        raise AppException("App not found")
    return app

@router.post("/create")
async def create_app(app: AppDTO):
    created_app = create_app(app)
    return { 'message': 'App created successfully', 'app': created_app.to_dict() }

@router.post("/project/create")
async def create_project(project: ProjectDTO):
    created_project = create_project(project)
    return {'message': 'Project created successfully', "project": created_project.to_dict()}

@router.post("/task/create")
async def create_task(task: TaskDTO):
    created_task = add_task_to_project(task)
    return {"task": created_task.to_dict()}

@router.delete("/task/{task_id}")
async def delete_task(task_id: int):
    remove_task(task_id)
    return {"message": "Task deleted successfully"}

@router.put("/task/{task_id}/release/{release_id}")
async def assign_release_to_task(task_id: int, release_id: int) -> TaskDTO:
    updated_task = assign_to_release(task_id, release_id)
    if not updated_task: 
        raise TaskException("Task not found")
    return {"task": updated_task.to_dict()}

@router.get("/task/backlog/{project_id}", response_model=List[TaskDTO])
async def backlog(project_id: int) -> List[TaskDTO]:
    tasks = get_backlog_tasks(project_id)
    return tasks

@router.get("/task/scheduled/{project_id}", response_model=List[TaskDTO])
async def scheduled(project_id: int) -> List[TaskDTO]:
    tasks = get_scheduled_tasks(project_id)
    return tasks

@router.delete("/project/{project_id}")
async def delete_project(project_id: int):
    remove_project(project_id)
    return {"message": "Project deleted successfully"}  

@router.delete("/{app_id}") 
async def delete_app(app_id: int):
    remove_app(app_id)
    return {"message": "App deleted successfully"}
