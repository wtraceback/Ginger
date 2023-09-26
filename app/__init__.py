from flask import Flask


def create_app():
    app = Flask(__name__)

    register_blueprints(app)

    return app


def register_blueprints(app):
    from app.api.v1.book import book
    app.register_blueprint(book)

    from app.api.v1.user import user
    app.register_blueprint(user)
