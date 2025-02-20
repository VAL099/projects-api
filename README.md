# Project Portfolio API

A Flask-based REST API for managing and presenting portfolio projects.

## Features
- JSON-based data storage
- GET endpoints for retrieving all projects and single project details
- Docker support for easy deployment

## Requirements
- Python 3.10+
- Flask
- Docker (optional)

## Installation & Setup

### Without Docker
1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   python run.py
   ```

### With Docker
1. Build and run using Docker Compose:
   ```bash
   docker-compose up --build
   ```

## API Endpoints

### GET /api/projects
Retrieves all projects.

Response format:
```json
{
    "projects": [
        {
            "id": "1",
            "name": "Project Name",
            "description": "Project Description",
            "technologies": ["Python", "Flask", "Docker"],
            "start_date": "2023-01-01",
            "end_date": "2023-12-31"
        }
    ]
}
```

### GET /api/projects/<project_id>
Retrieves a specific project by ID.

Response format:
```json
{
    "id": "1",
    "name": "Project Name",
    "description": "Project Description",
    "technologies": ["Python", "Flask", "Docker"],
    "start_date": "2023-01-01",
    "end_date": "2023-12-31"
}
```
