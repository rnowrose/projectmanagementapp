import uuid

def generate_unique_project_ref(app_name: str) -> str:
    app_initials = app_name[:3].upper()
    uuid = str(uuid.uuid3(uuid.NAMESPACE_DNS, app_name))
    app_id = uuid.split('-')[0]
    ref = f"{app_initials}-{app_id}"
    return ref

def generate_unique_task_ref(project_name: str) -> str:
    project_name_initials = project_name[:3].upper()
    project_id = str(uuid.uuid3(uuid.NAMESPACE_DNS, project_name))
    project_name_initials = project_name[:3].upper()
    ref = f"{project_name_initials}-{project_id.split('-')[0]}"
    return ref

def generate_app_code(app_name: str) -> str:
    unique_id = str(uuid.uuid3(uuid.NAMESPACE_DNS, app_name))
    code = unique_id.split('-')[0]
    return code