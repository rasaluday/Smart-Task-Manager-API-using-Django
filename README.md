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

## API Output Screenshots

1. GET /smart/tasks (List Tasks)

![GET Tasks](<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/c0fe504d-8958-4812-a96b-4b7dba206bbd" />
)

---

2. PATCH /smart/tasks/{id} (Mark Complete)

![PATCH Task](<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/cdc0f52b-8fe4-49a6-8362-32f04240aec0" />
)


