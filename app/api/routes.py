from flask_restx import Resource

from app.api.utils import read_projects
from app.api.models import project_model
from app.api.namespaces import api_ns


@api_ns.route('/projects')
class ProjectList(Resource):
    @api_ns.doc('list_projects')
    @api_ns.marshal_list_with(project_model)
    def get(self):
        """Get all projects"""
        try:
            return read_projects()
        except Exception as e:
            api_ns.abort(500, f'Failed to read projects. Error: {e}')


@api_ns.route('/projects/<int:project_id>')
@api_ns.param('project_id', 'The project identifier')
@api_ns.response(404, 'Project not found')
@api_ns.response(500, 'Internal Server Error - Data integrity issue')
class Project(Resource):
    @api_ns.doc('get_project')
    @api_ns.marshal_with(project_model)
    def get(self, project_id):
        """Get a specific project"""
        response = [project for project in read_projects() if project['id'] == project_id]
        if not response:
            api_ns.abort(404, f'Project {project_id} not found')
        elif len(response) > 1:
            api_ns.abort(500, f'Multiple projects found with id {project_id}. Found {len(response)} matches.')
        return response[0]
