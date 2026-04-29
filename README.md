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

## API Output Screenshots

1. GET /smart/tasks (List Tasks)
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/e2e7ed1c-a9c1-4ba2-b861-380590462f71" />


---

2. PATCH /smart/tasks/{id} (Mark Complete)

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/eb3ec88e-b478-4d6d-a42b-8ebba2b17332" />



## Run Project

```bash
pip install -r requirements.txt
python manage.py runserver




