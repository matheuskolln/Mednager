from flask import Flask
from infra.routes import routes


def create_app() -> Flask:
    app = Flask(__name__)
    register_routes(app)
    return app


def register_routes(app: Flask) -> None:
    app.register_blueprint(routes)


app = create_app()
