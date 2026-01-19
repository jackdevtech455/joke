from pydantic import BaseModel


class JokeFlags(BaseModel):
    nsfw: bool
    religious: bool
    political: bool
    racist: bool
    sexist: bool
    explicit: bool


class JokeRead(BaseModel):
    id: int
    error: str | bool
    category: str
    type: str
    setup: str
    delivery: str
    flags: JokeFlags
    safe: bool
    lang: str
