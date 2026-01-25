import requests

from joke_app.schemas.joke import JokeRead


def get_joke() -> JokeRead:
    joke = None

    while not joke:
        response = requests.get("https://v2.jokeapi.dev/joke/any")

        joke = JokeRead(**response.json())

        if not joke.setup and not joke.delivery:
            joke = None

    return joke
