from app import create_app, db
from app.models import User, Post, Notification, Message
from app import cli

app = create_app()
cli.register(app)


@app.shell_context_processor
def make_shell_context():
    return {
        "db": db,
        "User": User,
        "Post": Post,
        "Message": Message,
        "Notification": Notification,
    }
