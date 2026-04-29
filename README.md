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

## API Screenshot
1. GET /smart/tasks (List Tasks)
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/a2b9bf61-1ee8-40e6-960e-a575c02c53fa" />
----------
### 2. PATCH /smart/tasks/{id} (Mark Complete)
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/4bdbccb1-cbb3-4f1a-a399-b61e46d41e41" />


