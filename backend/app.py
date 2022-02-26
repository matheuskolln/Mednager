from flask import Flask
from infra.routes import routes
from config.populate import populate_plans
from config.extensions import db_session


def create_app() -> Flask:
    app = Flask(__name__)
    register_routes(app)
    populate()
    return app


def register_routes(app: Flask) -> None:
    app.register_blueprint(routes)


def populate() -> None:
    populate_plans(db_session)


app = create_app()
