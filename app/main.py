from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/joke")
def joke():
    response = requests.get("https://v2.jokeapi.dev/joke/any")
    return response.json()

