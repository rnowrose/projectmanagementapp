import type { Accomplishments, Education, Experience, LoginInfo, User, UserLogin } from "$lib/domain/Users.ts";
import { projectAxios } from "./axios.ts";

function login(loginData: UserLogin): Promise<LoginInfo> {
    return projectAxios.post<LoginInfo>('/users/login', loginData).then(response => response.data);
}

function getUserProfile(token: string): Promise<User> {
    return projectAxios.get<User>(`/users/profile`, {
        headers: {
            Authorization: `Bearer ${token}`
        }
    }).then(response => response.data);
}

function register(userData: Partial<User>): Promise<User> {
    return projectAxios.post<User>('/users/register', userData).then(response => response.data);
}

function updateUser(userData: Partial<User>, token: string): Promise<User> {
    return projectAxios.put<User>(`/users/profile`, userData, {
        headers: {
            Authorization: `Bearer ${token}`
        }
    }).then(response => response.data);
}

// Experience methods
function addExperience(experience: Partial<Experience>, token: string): Promise<Experience> {
    return projectAxios.post<Experience>('/users/experience', experience, {
        headers: {
            Authorization: `Bearer ${token}`
        }
    }).then(response => response.data);
}

function updateExperience(experienceId: number, experience: Partial<Experience>, token: string): Promise<Experience> {
    return projectAxios.put<Experience>(`/users/experience/${experienceId}`, experience, {
        headers: {
            Authorization: `Bearer ${token}`
        }
    }).then(response => response.data);
}

function deleteExperience(experienceId: number, token: string): Promise<{ message: string }> {
    return projectAxios.delete(`/users/experience/${experienceId}`, {
        headers: {
            Authorization: `Bearer ${token}`
        }
    }).then(response => response.data);
}

// Accomplishment methods
function addAccomplishment(accomplishment: Partial<Accomplishments>, token: string): Promise<Accomplishments> {
    return projectAxios.post<Accomplishments>('/users/accomplishment', accomplishment, {
        headers: {
            Authorization: `Bearer ${token}`
        }
    }).then(response => response.data);
}

function updateAccomplishment(accomplishmentId: number, accomplishment: Partial<Accomplishments>, token: string): Promise<Accomplishments> {
    return projectAxios.put<Accomplishments>(`/users/accomplishment/${accomplishmentId}`, accomplishment, {
        headers: {
            Authorization: `Bearer ${token}`
        }
    }).then(response => response.data);
}

function deleteAccomplishment(accomplishmentId: number, token: string): Promise<{ message: string }> {
    return projectAxios.delete(`/users/accomplishment/${accomplishmentId}`, {
        headers: {
            Authorization: `Bearer ${token}`
        }
    }).then(response => response.data);
}

// Education methods
function addEducation(education: Partial<Education>, token: string): Promise<Education> {
    return projectAxios.post<Education>('/users/education', education, {
        headers: {
            Authorization: `Bearer ${token}`
        }
    }).then(response => response.data);
}

function updateEducation(educationId: number, education: Partial<Education>, token: string): Promise<Education> {
    return projectAxios.put<Education>(`/users/education/${educationId}`, education, {
        headers: {
            Authorization: `Bearer ${token}`
        }
    }).then(response => response.data);
}

function deleteEducation(educationId: number, token: string): Promise<{ message: string }> {
    return projectAxios.delete(`/users/education/${educationId}`, {
        headers: {
            Authorization: `Bearer ${token}`
        }
    }).then(response => response.data);
}

function logout(token: string): Promise<void> {
    return projectAxios.post('/users/logout', {}, {
        headers: {
            Authorization: `Bearer ${token}`
        }
    });
}

export {
    addAccomplishment, addEducation, addExperience, deleteAccomplishment, deleteEducation, deleteExperience, getUserProfile, login, logout, register, updateAccomplishment, updateEducation, updateExperience, updateUser
};
