from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from joke_app.services.joke import get_joke

app = FastAPI()

app.mount(
    "/static",
    StaticFiles(directory="src/joke_app/static"),
    name="static",
)

templates = Jinja2Templates(directory="src/joke_app/templates")


@app.get("/", response_class=HTMLResponse)
def root(request: Request):
    joke = get_joke()

    return templates.TemplateResponse(
        name="joke.html",
        context={
            "request": request,
            "joke": joke,
        },
        #            "setup": joke.setup,
        #   "delivery": joke.delivery,
        # },
    )
