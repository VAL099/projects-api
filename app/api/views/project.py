from api.utils import read_projects_from_json
from flask_restx import Resource
from api.namespaces import api_ns
from api.models.project import project


@api_ns.route('/projects')
class ProjectList(Resource):
    @api_ns.doc('list_projects')
    @api_ns.marshal_list_with(project)
    def get(self):
        """Get all projects"""
        try:
            return read_projects_from_json()
        except Exception as e:
            api_ns.abort(500, f'Failed to read projects. Error: {e}')


@api_ns.route('/projects/<int:project_id>')
@api_ns.param('project_id', 'The project identifier')
@api_ns.response(404, 'Project not found')
@api_ns.response(500, 'Internal Server Error - Data integrity issue')
class Project(Resource):
    @api_ns.doc('get_project')
    @api_ns.marshal_with(project)
    def get(self, project_id):
        """Get a specific project by id"""
        response = [project for project in read_projects_from_json() if project['id'] == project_id]
        if not response:
            api_ns.abort(404, f'Project {project_id} not found')
        elif len(response) > 1:
            api_ns.abort(500, f'Multiple projects found with id {project_id}. Found {len(response)} matches.')
        return response[0]
