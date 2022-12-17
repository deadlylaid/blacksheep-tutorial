from blacksheep import Application

app = Application()


@app.router.get("/")
def home() -> str:
    return 'Hello World'


posts_app = Application()


@posts_app.router.get("/")
def posts() -> dict:
    return {
        'posts': [
            {'post_id': 1, 'name': 'post_1', 'url': '/posts/image1.jpg'},
            {'post_id': 2, 'name': 'post_2', 'url': '/posts/image2.jpg'}
        ]
    }


app.mount_registry.auto_events = True
app.mount("/posts", posts_app)
