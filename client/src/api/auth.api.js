import axios from 'axios';

const backendUrl = import.meta.env.VITE_BACKEND_URL || "http://localhost:3000";

const api = axios.create({
    baseURL: `${backendUrl}/api/auth`,
    withCredentials: true
})



// register
export const registerHandler = async ({name, email, password}) => {
    const response = await api.post("/register", { name, email, password });
    return response.data;
}


// login
export const loginHandler = async ({email, password}) => {
    const response = await api.post("/login", { email, password });
    return response.data;
}

// logout
export const logoutHandler = async () => {
    const response = await api.post("/logout");
    return response.data;
}