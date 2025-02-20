from flask_restx import fields

from app.api.namespaces import api_ns

project_model = api_ns.model(
    name='Project',
    model={
        'id': fields.Integer(readOnly=True, description='The project unique identifier'),
        'name': fields.String(required=True, description='The project name'),
        'description': fields.String(required=True, description='The project description'),
        'technologies_used': fields.List(
            cls_or_instance=fields.String, required=True, description='The technologies used in the project'
        ),
        'start_date': fields.DateTime(readOnly=True, description='The date/time the project was created'),
        'end_date': fields.DateTime(
            allow_none=True, readOnly=True, description='The date/time the project was last updated'
        ),
    },
)
