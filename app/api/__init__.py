from flask import Flask
from flask_restx import Api


def create_app():
    from . import routes

    app = Flask(__name__)
    api = Api(
        app, title='Projects API', version='1.0', description='A simple API to manage projects', doc='/docs'
    )
    api.add_namespace(routes.api_ns)

    return app
