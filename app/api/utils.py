import os
import json


def read_projects() -> dict:
    base_dir = os.path.dirname(os.path.dirname(__file__))
    file_path = os.path.join(base_dir, 'data', 'projects.json')

    with open(file_path, 'r', encoding='utf-8') as file:
        projects = json.load(file)
    return projects
