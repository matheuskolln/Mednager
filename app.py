from flask import Flask
from infra.routes import routes
from config.populate import populate
from config.extensions import db_session


def create_app() -> Flask:
    app = Flask(__name__)
    register_routes(app)
    populate(db_session)
    return app


def register_routes(app: Flask) -> None:
    app.register_blueprint(routes)


app = create_app()
