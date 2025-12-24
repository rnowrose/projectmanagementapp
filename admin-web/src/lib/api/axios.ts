import axios from 'axios';


const projectAxios = axios.create({
  baseURL: import.meta.env.VITE_PROJECT_API_URL,
  headers: {
    'Content-Type': 'application/json',
    'X-Application': 'Project Management API',
  },
});

export {
    projectAxios,
}