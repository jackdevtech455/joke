from fastapi import FastAPI

from joke_app.services.joke import get_joke

app = FastAPI()


@app.get("/")
def root():
    joke = get_joke()

    return joke
