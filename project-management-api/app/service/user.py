from peewee import *
from app.models import Users,Experiences, Clients,Education,Accomplishment
from app.util.exceptions import UserException
from typing import Optional
from app.dto.users import UserDTO
from app.db.database import log

def login(username: str, password: str) -> Optional[Users]:
    auth_user = Users.authenticate(username, password)
    if auth_user:
        user = Users.get(Users.username == username)
        return user
    raise UserException('Invalid username or password')

def create_user(user: UserDTO) -> UserDTO:
    name = user.full_name.split(' ')
    new_user = Users.create(
        username=user.username,
        hashed_password=Users.hash_password(user.password),
        first_name=name[0],
        last_name=name[1] if len(name) > 1 else '',
        is_active=True,
        email=user.email,
        phone_number=user.phone_number
    )
    
    return UserDTO(
        id=new_user.id,
        username=new_user.username,
        fullName=new_user.full_name,
        password="",
        email=new_user.email,
        phoneNumber=new_user.phone_number,
        is_active=new_user.is_active,
        experience=[],
        education=[],
        clients=[]
    )

def profile(user_id: int) -> Optional[UserDTO]:
    user = Users.get_or_none(Users.id == user_id)
    education = list(Education.select().where(Education.user_id == user_id))
    experience = list(Experiences.select().where(Experiences.user_id == user_id))
    accomplishments = list(Accomplishment.select().where(Accomplishment.user_id == user_id))
    client = list(Clients.select().where(Clients.user_id == user_id))
    if not user:
        raise UserException('user not found')
    return UserDTO(
        id=user.id,
        username=user.username,
        fullName=user.full_name,
        password="",
        email=user.email,
        phoneNumber=user.phone_number,
        experience=experience,
        education=education,
        accomplishments=accomplishments,
        clients=client
    )

def update_profile(user_id: int, user_data: UserDTO) -> Users:
    user = Users.get_or_none(Users.id == user_id)
    if not user:
        raise UserException('user not found')
    fullname_segments = user_data.full_name.split(' ')
    user.first_name = fullname_segments[0]
    user.last_name = fullname_segments[1] if len(fullname_segments) > 1 else ''
    user.email = user_data.email
    user.phone_number = user_data.phone_number
    user.save()
        # Fetch related data
    education = list(Education.select().where(Education.user_id == user_id))
    experience = list(Experiences.select().where(Experiences.user_id == user_id))
    accomplishments = list(Accomplishment.select().where(Accomplishment.user_id == user_id))
    clients = list(Clients.select().where(Clients.user_id == user_id))
    
    return UserDTO(
        id=user.id,
        username=user.username,
        fullName=user.full_name,
        password="",
        email=user.email,
        phoneNumber=user.phone_number,
        experience=experience,
        education=education,
        accomplishments=accomplishments,
        clients=clients
    )

def insert_client_profile(client_data, user_id: int) -> Clients:
    client = Clients.create(
        name=client_data.name,
        contact_email=client_data.contact_email,
        phone_number=client_data.phone_number,
        address=client_data.address,
        user_id=user_id
    )
    return client

def update_client_profile(client_id: int, client_data) -> Clients:
    client = Clients.get_or_none(Clients.id == client_id)
    if not client:
        raise UserException('client not found')
    client.name = client_data.name
    client.contact_email = client_data.contact_email
    client.phone_number = client_data.phone_number
    client.address = client_data.address
    client.save()
    return client

def insert_education_profile(education_data, user_id: int) -> Education:
    education = Education.create(
        degree=education_data.degree,
        location=education_data.location,
        institution=education_data.institution,
        start_date=education_data.start_date,
        end_date=education_data.end_date,
        description=education_data.description,
        user_id=user_id
    )
    return education

def update_education_profile(education_id: int, education_data) -> Education:
    education = Education.get_or_none(Education.id == education_id)
    if not education:
        raise UserException('education not found')
    education.degree = education_data.degree
    education.location = education_data.location
    education.institution = education_data.institution
    education.start_date = education_data.start_date
    education.end_date = education_data.end_date
    education.description = education_data.description
    education.save()
    return education

def delete_education_profile(education_id: int) -> None:
    education = Education.get_or_none(Education.id == education_id)
    if not education:
        raise UserException('education not found')
    education.delete_instance()

def delete_experience_profile(experience_id: int) -> None:
    experience = Experiences.get_or_none(Experiences.id == experience_id)
    if not experience:
        raise UserException('experience not found')
    experience.delete_instance()

def insert_experience_profile(experience_data, user_id: int) -> Experiences:
    experience = Experiences.create(
        title=experience_data.title,
        company_name=experience_data.company,
        location=experience_data.location,
        start_date=experience_data.start_date,
        end_date=experience_data.end_date,
        description=experience_data.description,
        user_id=user_id
    )
    return experience

def update_experience_profile(experience_id: int, experience_data) -> Experiences:
    experience = Experiences.get_or_none(Experiences.id == experience_id)
    if not experience:
        raise UserException('experience not found')
    experience.title = experience_data.title
    experience.location = experience_data.location
    experience.company = experience_data.company
    experience.start_date = experience_data.start_date
    experience.end_date = experience_data.end_date
    experience.description = experience_data.description
    experience.save()
    return experience

def delete_experience_profile(experience_id: int) -> None:
    experience = Experiences.get_or_none(Experiences.id == experience_id)
    if not experience:
        raise UserException('experience not found')
    experience.delete_instance()

def insert_accomplishment_profile(accomplishment_data, user_id: int) -> Accomplishment:
    accomplishment = Accomplishment.create(
        title=accomplishment_data.title,
        description=accomplishment_data.description,
        date_achieved=accomplishment_data.date_achieved,
        accomplishment_type=accomplishment_data.accomplishment_type,
        user_id=user_id
    )
    return accomplishment

def update_accomplishment_profile(accomplishment_id: int, accomplishment_data) -> Accomplishment:
    accomplishment = Accomplishment.get_or_none(Accomplishment.id == accomplishment_id)
    if not accomplishment:
        raise UserException('accomplishment not found')
    accomplishment.title = accomplishment_data.title
    accomplishment.description = accomplishment_data.description
    accomplishment.date_achieved = accomplishment_data.date_achieved
    accomplishment.accomplishment_type = accomplishment_data.accomplishment_type
    accomplishment.save()
    return accomplishment

def delete_accomplishment_profile(accomplishment_id: int) -> None:
    accomplishment = Accomplishment.get_or_none(Accomplishment.id == accomplishment_id)
    if not accomplishment:
        raise UserException('accomplishment not found')
    accomplishment.delete_instance()

def logout(user: Users) -> None:
    if not user:
        raise UserException('user not found')
    user.token = None
    user.save()