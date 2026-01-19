import requests

from joke_app.schemas.joke import JokeRead


def get_joke() -> JokeRead:
    response = requests.get("https://v2.jokeapi.dev/joke/any")

    joke = JokeRead(**response.json())

    return joke
