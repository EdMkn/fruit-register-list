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

## Usage

- Open the frontend in your browser.
- Add fruits using the provided form.
- The frontend communicates with the FastAPI backend to store and display the list of fruits. 