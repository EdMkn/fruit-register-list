# FastAPI Fruits Registration Web App

## Project Intent

This project is designed to help you get familiarized with FastAPI, a modern, fast (high-performance) web framework for building APIs with Python 3.7+.

## Project Description

This is a simple web application that allows users to register fruits. The backend is built with FastAPI and provides endpoints to add and list fruits. The frontend is built with React and interacts with the backend to display and register fruits inputted by the user.

## Getting Started

### Prerequisites

- Python 3.7+
- Node.js (v18+ recommended) and npm

---

## Running the Backend (FastAPI)

1. **Install dependencies:**

   ```bash
   cd backend
   pip install -r requirements.txt
   ```

2. **Start the FastAPI server (default port: 8000):**

   ```bash
   python main.py
   ```

   The API will be available at [http://localhost:8000](http://localhost:8000).

---

## Running the Frontend (React)

1. **Install dependencies:**

   ```bash
   cd frontend
   npm install
   ```

2. **Start the React development server (default port: 5173):**

   ```bash
   npm run dev
   ```

   The app will be available at [http://localhost:5173](http://localhost:5173).

---

## Running with Docker Compose

You can run both the backend and frontend together using Docker Compose. This is the recommended way to run the project in a production-like environment.

1. **Build and start the services:**

   ```bash
   docker-compose up --build
   ```

   - The backend will be available at [http://localhost:9000](http://localhost:9000)
   - The frontend will be available at [http://localhost:3000](http://localhost:3000)

2. **Stopping the services:**

   Press `Ctrl+C` to stop, then run:
   ```bash
   docker-compose down
   ```

---

## CORS Configuration for Docker Compose

When running the frontend and backend with Docker Compose, make sure your backend CORS settings include the following origins in `backend/main.py`:

```python
origins = [
    "http://localhost:5173",           # dev local hors Docker
    "http://fruits-frontend:3000",     # depuis Docker Compose
    "http://localhost:3000"            # frontend via Docker Compose on host
]
```

This allows the frontend (served from `http://localhost:3000`) to communicate with the backend without CORS issues.

---

## Usage

- Open the frontend in your browser.
- Add fruits using the provided form.
- The frontend communicates with the FastAPI backend to store and display the list of fruits. 