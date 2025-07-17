import axios from 'axios'

//creates an instance of axios with the base URL
const api = axios.create({
    baseURL: "http://localhost:9000"}
)

export default api;
