from datetime import datetime
from blacksheep import Application, Request
from typing import List

app = Application()
get = app.router.get
post = app.router.post
delete = app.router.delete


@app.route("/some-route")
def home() -> datetime:
    return datetime.now()


@get("/{one}/{two}/{three}")
def ex_post(one: str, two: str, three: str) -> str:
    return f'Hello {one} {two} {three}'


@get("/query-list")
def the_list(name: List[str]) -> str:
    return f"Hello {' '.join(name)}"


@get("/request")
def the_request(request: Request) -> str:
    return 'a'


@get("/{name}")
def ex_get(name) -> str:
    return f'Hello {name}'


@delete("/")
def ex_delete() -> str:
    return 'deleted'
