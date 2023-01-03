from blacksheep import Application
from typing import Dict, List, TypedDict

app = Application()


class PostTypedDict(TypedDict):
    post_id: int
    name: str
    url: str


@app.router.get("/")
def home() -> str:
    return 'Hello World'


posts_app = Application()


@posts_app.router.get("/")
def posts() -> Dict[str, List[PostTypedDict]]:
    return {
        'posts': [
            {'post_id': 1, 'name': 'post_1', 'url': '/posts/image1.jpg'},
            {'post_id': 2, 'name': 'post_2', 'url': '/posts/image2.jpg'}
        ]
    }


@posts_app.router.get("/1")
def posts_detail() -> PostTypedDict:
    return {'post_id': 1, 'name': 'post_1', 'url': '/posts/image1.jpg'}


app.mount_registry.auto_events = True
app.mount("/posts", posts_app)
