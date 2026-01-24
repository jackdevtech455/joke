import requests

from joke_app.schemas.joke import JokeRead


def get_joke() -> JokeRead:
    joke_setup = ""
    joke_delivery = ""

    while not joke_setup and not joke_delivery:
        response = requests.get("https://v2.jokeapi.dev/joke/any")

        joke = JokeRead(**response.json())

        joke_setup = joke.setup
        joke_delivery = joke.delivery

    return joke
