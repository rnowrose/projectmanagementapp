from typing import List
from pydantic import BaseModel
from app.dto.base_schema import BaseSchema


class AppDTO(BaseSchema):
   id: int
   name: str
   code_name: str
   timestamp: str
   description: str
   created_at: str
   updated_at: str
   work_type: str
   host: str
   user_id: int

class ProjectDTO(BaseSchema):
    id: int
    project_ref: str
    name: str
    start_date: str
    end_date: str
    timestamp: str
    description: str
    created_at: str
    updated_at: str
    release: str
    app: AppDTO

class TaskDTO(BaseSchema):
   id: int
   task_ref: str
   name: str
   story: str
   days: int
   status: str
   priority: str
   created_at: str
   updated_at: str
   project: ProjectDTO
   
class ReleaseDTO(BaseSchema):
    id: int
    name: str
    version: str
    description: str
    release_date: str
    created_at: str
    updated_at: str
    tasks: List[str]  

   