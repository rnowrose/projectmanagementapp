import { browser } from '$app/environment';
import { addAccomplishment, addEducation, addExperience, deleteAccomplishment, deleteExperience, getUserProfile, login, logout, register, updateAccomplishment, updateEducation, updateUser } from '$lib/api/users.api.ts';
import type { Accomplishments, Education, Experience, LoginInfo, User, UserLogin } from '$lib/domain/Users.ts';
import { get, writable } from 'svelte/store';

interface AuthState {
    isAuthenticated: boolean;
    loginInfo: LoginInfo | null;
}

function loadAuthState(): AuthState {
    if (browser) {
        const stored = localStorage.getItem('authState');
        if (stored) {
            try {
                return JSON.parse(stored);
            } catch (e) {
                console.error('Failed to parse stored auth state:', e);
            }
        }
    }
    return {
        isAuthenticated: false,
        loginInfo: null
    };
}

function createUserStore() {
    const { subscribe, set, update } = writable<AuthState>(loadAuthState());

    subscribe((state) => {
        if (browser) {
            localStorage.setItem('authState', JSON.stringify(state));
        }
    });

    return {
        subscribe,
        async login(userLogin: UserLogin): Promise<LoginInfo | null> { 
            try {
                const response = await login(userLogin);
                update(state => ({
                    ...state,
                    isAuthenticated: true,
                    loginInfo: response
                }));
                return response;
            } catch (error) {
                console.error('Login error:', error);
                return null;
            }
        },
        async logout(): Promise<void> {
            const token = get(userStore).loginInfo?.token;
            if (token) await logout(token);
            if (browser) localStorage.removeItem('authState');
            set({
                isAuthenticated: false,
                loginInfo: null
            });

        },
        async profile(): Promise<User | null> {
            const token = get(userStore).loginInfo?.token;
            if (token) {
                try {
                    const userProfile = await getUserProfile(token);
                    update(state => ({ ...state }));
                    return userProfile;
                } catch (error) {
                    console.error('Profile fetch error:', error);
                    return null;
                }
            }
            return null;
        },
        async createUser(user: Partial<User>): Promise<void> {
            try {
                const newUser = await register(user);
            update(state => ({ ...state, user: newUser }) );
            } catch (error) {
                console.error('Create user error:', error);
            }
        },
        async updateUser(user: Partial<User>): Promise<User | null> {
            const token = get(userStore).loginInfo?.token;
            if (token) {
                try {
                    const updatedUser = await updateUser(user, token);
                    update(state => ({ ...state, user: updatedUser }));
                    return updatedUser;
                } catch (error) {
                    console.error('Update user error:', error);
                    return null;
                }
            }
            return null;
        },
        async upsertExperience(experience: Partial<Experience>): Promise<Experience | null> {
            const token = get(userStore).loginInfo?.token;
            if (token) {
                try {
                    if (experience) {
                        // Update existing experience
                        const updatedExperience = await updateUser(experience, token);
                        // Optionally update the user store with the updated experience
                        update(state => {
                            if (state.user && state.user.experience && updatedExperience) {
                                const updatedExperiences = state.user.experience.map(exp =>
                                    exp.id === experience.id ? experience as Experience : exp
                                );
                                return {
                                    ...state,
                                    user: { ...state.user, experience: updatedExperiences }
                                };
                            }
                            return state;
                        });
                        return experience as Experience;
                    } else {
                        const newExperience = await addExperience(experience, token);
                        // Optionally update the user store with the new experience
                        update(state => {
                            if (state.user) {
                                const updatedExperiences = state.user.experience ? [...state.user.experience, newExperience] : [newExperience];
                                return {
                                    ...state,
                                    user: { ...state.user, experience: updatedExperiences }
                                };
                            }
                            return state;
                        });
                        return newExperience;
                 }
                } catch (error) {
                    console.error('Add experience error:', error);
                    return null;
                }
            }
            return null;
        },
        async deleteExperience(experienceId: number): Promise<boolean> {
            const token = get(userStore).loginInfo?.token;
            if (token) {
                try {
                    await deleteExperience(experienceId, token);
                    // Optionally update the user store to remove the deleted experience
                    update(state => {
                        if (state.user && state.user.experience) {
                            const updatedExperiences = state.user.experience.filter(exp => exp.id !== experienceId);
                            return {
                                ...state,
                                user: { ...state.user, experience: updatedExperiences }
                            };
                        }
                        return state;
                    });
                    return true;
                } catch (error) {
                    console.error('Delete experience error:', error);
                    return false;
                }
            }
            return false;
        },
        async upsertAccomplishment(accomplishment: Partial<Accomplishments>): Promise<Accomplishments | null> {
            const token = get(userStore).loginInfo?.token;
            if (token) {
                try {
                    if (accomplishment) {
                        const update = await updateAccomplishment(accomplishment.id!, accomplishment, token);
                        return update;
                       
                    } else {
                        const add = await addAccomplishment(accomplishment, token);
                        return add;
                    }
                } catch (error) {
                    console.error('Upsert accomplishment error:', error);
                    return null;
                }
            }
            return null;
            
        },
        async deleteAccomplishment(accomplishmentId: number): Promise<boolean> {
            const token = get(userStore).loginInfo?.token;
            if (token) {
                try {
                    // Assuming deleteAccomplishment function exists in the API
                    await deleteAccomplishment(accomplishmentId, token);
                    return true;
                } catch (error) {
                    console.error('Delete accomplishment error:', error);
                    return false;
                }
            }
            return false;
        },
        async upsertEducation(education: Partial<Education>): Promise<Education | null> {
            const token = get(userStore).loginInfo?.token;
            if (token) {
                try {
                    if (education.id) {
                        // Update existing education
                        const updatedEducation = await updateEducation(education.id!, education, token);
                        return updatedEducation;
                    } else {
                        const newEducation = await addEducation(education, token);
                        return newEducation;
                 }
                } catch (error) {
                    console.error('Add education error:', error);
                    return null;
                }
            }
            return null;
        },
        async deleteEducation(educationId: number): Promise<boolean> {
            const token = get(userStore).loginInfo?.token;
            if (token) {
                try {
                    await deleteExperience(educationId, token);
                    return true;
                } catch (error) {
                    console.error('Delete education error:', error);
                    return false;
                }
            }
            return false;
        },
        setUser(user: User) {
            update(state => ({ ...state, user }));
        }
    };
}

export const userStore = createUserStore();
