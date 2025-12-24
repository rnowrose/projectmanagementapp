from typing import List, Optional
from app.dto.base_schema import BaseSchema

class ExperienceDTO(BaseSchema):
    id: int
    title: str
    location: str
    company: str
    start_date: str
    end_date: str
    description: str
    user_id: int
    
class EducationDTO(BaseSchema):
    id: int
    degree: str
    location: str
    institution: str
    start_date: str
    end_date: Optional[str] = None
    description: str
    user_id: int

class AccomplishmentDTO(BaseSchema):
    id: int
    title: str
    description: str
    date_achieved: str
    accomplishment_type: str
    user_id: int

class UserLoginDTO(BaseSchema):
    username: str
    password: str

class LoginInfo(BaseSchema):
    user_id: int
    token: str
    success: bool
    message: str
    
class ClientDTO(BaseSchema):
    id: int
    name: str
    contact_email: str
    phone_number: str
    address: str
    user_id: int

class AccomplishmentDTO(BaseSchema):
    id: int
    title: str
    description: str
    date_achieved: str
    accomplishment_type: str
    user_id: int

class UserDTO(BaseSchema):
    id: Optional[int] = None
    username: str
    full_name: str
    password: Optional[str] = None
    email: str
    phone_number: Optional[str] = None
    summary: Optional[str] = None
    profile_picture: Optional[str] = None
    linkedin_url: Optional[str] = None
    github_url: Optional[str] = None
    website_url: Optional[str] = None
    experience: Optional[List[ExperienceDTO]] = None
    education: Optional[List[EducationDTO]] = None
    accomplishments: Optional[List[AccomplishmentDTO]] = None