from datetime import datetime
from unittest.mock import patch

import pytest
from api import create_app


@pytest.fixture
def sample_projects():
    return [
        {
            'id': 1,
            'name': 'Test Project 1',
            'description': 'First test project',
            'technologies_used': ['Python', 'Flask'],
            'start_date': datetime(2024, 1, 1),
            'end_date': datetime(2024, 2, 1),
        },
        {
            'id': 2,
            'name': 'Test Project 2',
            'description': 'Second test project',
            'technologies_used': ['React', 'Node.js'],
            'start_date': datetime(2024, 2, 1),
            'end_date': None,
        },
    ]


@pytest.fixture()
def app():
    _app = create_app()
    return _app


@pytest.fixture()
def client(app):
    return app.test_client()


class TestProjectList:
    @patch('api.views.project.read_projects_from_json')
    def test_get_projects_success(self, mock_read_projects_from_json, client, sample_projects):
        """Test successful retrieval of all projects"""
        mock_read_projects_from_json.return_value = sample_projects

        response = client.get('/api/projects')

        assert response.status_code == 200
        assert len(response.json) == 2
        assert response.json[0]['name'] == 'Test Project 1'
        assert response.json[1]['name'] == 'Test Project 2'

    @patch('api.views.project.read_projects_from_json')
    def test_get_projects_empty(self, mock_read_projects_from_json, client):
        """Test getting projects when none exist"""
        mock_read_projects_from_json.return_value = []

        response = client.get('/api/projects')

        assert response.status_code == 200
        assert len(response.json) == 0

    @patch('api.views.project.read_projects_from_json')
    def test_get_projects_error(self, mock_read_projects_from_json, client):
        """Test error handling when reading projects fails"""
        mock_read_projects_from_json.side_effect = Exception('Database error')

        response = client.get('/api/projects')

        assert response.status_code == 500
        assert 'Database error' in response.json['message']


class TestProject:
    @patch('api.views.project.read_projects_from_json')
    def test_get_project_success(self, mock_read_projects_from_json, client, sample_projects):
        """Test successful retrieval of a specific project"""
        mock_read_projects_from_json.return_value = sample_projects

        response = client.get('/api/projects/1')

        assert response.status_code == 200
        assert response.json['id'] == 1
        assert response.json['name'] == 'Test Project 1'
        assert len(response.json['technologies_used']) == 2

    @patch('api.views.project.read_projects_from_json')
    def test_get_project_not_found(self, mock_read_projects_from_json, client, sample_projects):
        """Test getting a non-existent project"""
        mock_read_projects_from_json.return_value = sample_projects

        response = client.get('/api/projects/999')

        assert response.status_code == 404
        assert 'Project 999 not found' in response.json['message']

    @patch('api.views.project.read_projects_from_json')
    def test_get_project_duplicate_id(self, mock_read_projects_from_json, client):
        """Test error handling when duplicate project IDs exist"""
        duplicate_projects = [
            {
                'id': 1,
                'name': 'Duplicate Project 1',
                'description': 'First duplicate',
                'technologies_used': ['Python'],
                'start_date': datetime(2024, 1, 1),
                'end_date': None,
            },
            {
                'id': 1,
                'name': 'Duplicate Project 2',
                'description': 'Second duplicate',
                'technologies_used': ['Java'],
                'start_date': datetime(2024, 1, 1),
                'end_date': None,
            },
        ]
        mock_read_projects_from_json.return_value = duplicate_projects

        response = client.get('/api/projects/1')

        assert response.status_code == 500
        assert 'Multiple projects found with id 1' in response.json['message']

    @patch('api.views.project.read_projects_from_json')
    def test_get_project_invalid_id(self, mock_read_projects_from_json, client, sample_projects):
        """Test getting a project with invalid ID format"""
        mock_read_projects_from_json.return_value = sample_projects
