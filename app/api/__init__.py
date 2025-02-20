from flask import Flask
from flask_restx import Api

from api.views import project


def create_app():
    app = Flask(__name__)
    api = Api(
        app, title='Projects API', version='1.0', description='A simple API to manage projects', doc='/docs'
    )
    api.add_namespace(project.api_ns)

    return app
