import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

class Fruit(BaseModel):
    name: str

class Fruits(BaseModel):
    fruits: List[Fruit]

app = FastAPI()

origins = [
    "http://localhost:5173",           # dev local hors Docker
    #"http://fruits-frontend:3000"      # depuis Docker Compose
    "http://localhost:3000"            # frontend via Docker Compose on host
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

memory_db = {"fruits" : []}

@app.get("/fruits", response_model=Fruits)
def get_fruits():
    return Fruits(fruits=memory_db["fruits"])

@app.post("/fruits", response_model=Fruits)
def add_fruit(fruit: Fruit):
    memory_db["fruits"].append(fruit)
    return Fruits(fruits=memory_db["fruits"])

#if __name__ == "__main__":
#   uvicorn.run(app, host="0.0.0.0",port=8000)
#*/