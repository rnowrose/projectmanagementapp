from fastapi import APIRouter, Depends, HTTPException
from app.service.user import *
from app.dto.users import AccomplishmentDTO, EducationDTO, ExperienceDTO, LoginInfo, UserDTO, UserLoginDTO
from app.util.auth_requried import create_access_token, get_current_user
from app.db.database import log

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/login", response_model=LoginInfo)
async def authenticate(user_login: UserLoginDTO):
    auth = login(user_login.username, user_login.password)
    if not auth:
        login_info = LoginInfo(token="", userId=0, success=False, message="Invalid username or password")
        raise HTTPException(status_code=401, detail=login_info["message"])
    token = create_access_token(subject=auth.id)
    auth.token = token
    auth.save()
    login_info = LoginInfo(token=token, userId=auth.id, success=True, message="Login successful", expired_at=None)
    return login_info

@router.post("/register", response_model=UserDTO)
async def register(user: UserDTO):
    new_user = create_user(user)
    return new_user
    
@router.get("/profile", response_model=UserDTO)
async def get_profile(current_user: Users = Depends(get_current_user)):
    user = profile(current_user.id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/profile", response_model=UserDTO)
async def update_user_profile(user_data: UserDTO, current_user: Users = Depends(get_current_user)):
    updated_user = update_profile(current_user.id, user_data)
    return updated_user

@router.post("/experience", response_model=ExperienceDTO)
async def add_experience(experience_data: ExperienceDTO, current_user: Users = Depends(get_current_user)):
    new_experience = insert_experience_profile(experience_data, current_user.id)
    return new_experience

@router.put("/experience/{experience_id}", response_model=ExperienceDTO)
async def update_experience(experience_id: int, experience_data: ExperienceDTO, current_user: Users = Depends(get_current_user)):
    updated_experience = update_experience_profile(experience_id, experience_data)
    return updated_experience

@router.delete("/experience/{experience_id}")
async def delete_experience(experience_id: int, current_user: Users = Depends(get_current_user)):
    delete_experience_profile(experience_id)
    return {"message": "Experience deleted successfully"}

@router.post("/accomplishment", response_model=AccomplishmentDTO)
async def add_accomplishment(accomplishment_data: AccomplishmentDTO, current_user: Users = Depends(get_current_user)):
    new_accomplishment = insert_accomplishment_profile(accomplishment_data, current_user.id)
    return new_accomplishment

@router.put("/accomplishment/{accomplishment_id}", response_model=AccomplishmentDTO)
async def update_accomplishment(accomplishment_id: int, accomplishment_data: AccomplishmentDTO, current_user: Users = Depends(get_current_user)):
    updated_accomplishment = update_accomplishment_profile(accomplishment_id, accomplishment_data)
    return updated_accomplishment

@router.delete("/accomplishment/{accomplishment_id}")
async def delete_accomplishment(accomplishment_id: int, current_user: Users = Depends(get_current_user)):
    delete_accomplishment_profile(accomplishment_id)
    return {"message": "Accomplishment deleted successfully"}

@router.post("/education", response_model=EducationDTO)
async def add_education(education_data: EducationDTO, current_user: Users = Depends(get_current_user)):
    new_education = insert_education_profile(education_data, current_user.id)
    return new_education

@router.put("/education/{education_id}", response_model=EducationDTO)
async def update_education(education_id: int, education_data: EducationDTO, current_user: Users = Depends(get_current_user)):
    updated_education = update_education_profile(education_id, education_data)
    return updated_education

@router.delete("/education/{education_id}")
async def delete_education(education_id: int, current_user: Users = Depends(get_current_user)):
    delete_education_profile(education_id)
    return {"message": "Education deleted successfully"}

@router.post("/logout")
async def end_session(current_user: Users = Depends(get_current_user)):
    logout(current_user)
    return {"message": "Logout successful"}