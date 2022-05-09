import os

from flask import Flask


def create_app():
    # create and configure the app with flask
    app = Flask(__name__)

    app.config.from_mapping(
        SECRET_KEY = 'developer',
        DATABASE_HOST = os.environ.get('FLASK_DATABASE_HOST'),
        DATABASE_USER = os.environ.get('FLASK_DATABASE_USER'),
        DATABASE_PASSWORD = os.environ.get('FLASK_DATABASE_PASSWORD'),
        DATABASE = os.environ.get('FLASK_DATABASE'),
    )

    from . import db

    db.init_app(app)


    from . import auth
    app.register_blueprint(auth.bp)

    from . import todo
    app.register_blueprint(todo.bp)


    @app.route('/hola')
    def hola():
        return 'Hola!!'


    return app
