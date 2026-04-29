# Smart Task Manager API

This project is a simple backend API built using Django REST Framework.

## Features

- Create a new task
- List all tasks
- Mark task as completed
- Auto-priority suggestion (AI-inspired feature)

## Tech Stack

- Python
- Django
- Django REST Framework

## Why Django?

I chose Django because I am comfortable with it and can build a clean API quickly within the time constraint.

## Smart Feature

Auto-priority suggestion:
- High → urgent, deadline, ASAP
- Medium → review, meeting, follow up
- Low → default

## API Endpoints

### Create Task
POST /smart/tasks

### List Tasks
GET /smart/tasks

### Complete Task
PATCH /smart/tasks/{id}

## Run Project

```bash
pip install -r requirements.txt
python manage.py runserver
