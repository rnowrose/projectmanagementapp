export interface User {
    id: number;
    username: string;
    password: string;
    email: string;
    phoneNumber?: string;
    fullName: string;
    summary?: string;
    githubUrl?: string;
    linkedinUrl?: string;
    websiteUrl?: string;
    profilePicture?: string;
    education?: Education[];
    experience?: Experience[];
    accomplishments?: Accomplishments[];
}

export interface UserLogin {
    username: string;
    password: string;
}

export interface LoginInfo {
    userId: number;
    token: string;
    success: boolean;
    message: string;
}

export interface Education {
    id: number;
    userId: number;
    location: string;
    institution: string;
    degree: string;
    fieldOfStudy: string;
    startDate: string;
    endDate: string;
    grade: string;
    description: string;

}
export interface Experience {
    id: number;
    userId: number;
    company: string;
    location: string;
    position: string;
    startDate: string;
    endDate: string;
    description: string;
}

export interface Accomplishments {
    id: number;
    userId: number;
    title: string;
    description: string;
    date: string;
}

export type MessageType = 'success' & 'error' & 'info' & 'warning'
export type Message = Record<MessageType, string>;