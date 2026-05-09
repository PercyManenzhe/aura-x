import axios from "axios";

const API = axios.create({
  baseURL: "http://127.0.0.1:8000",
});

export const runWorkflow = (data) =>
  API.post("/workflows/run", data);

export const getHealth = () =>
  API.get("/health");