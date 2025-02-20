#!/bin/bash

echo "Running pre-commit script"

ruff check --fix
echo "Code linted!"

ruff format 
echo "Code formatted!"

uv pip freeze > requirements.txt
echo "Requirements compiled!"
