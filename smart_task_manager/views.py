from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

tasks = []
task_id_counter = 1


def suggest_priority(title, description):
    text = f"{title} {description}".lower()

    high_keywords = ["urgent", "asap", "deadline", "critical", "important", "today"]
    medium_keywords = ["soon", "tomorrow", "review", "follow up", "meeting"]

    if any(word in text for word in high_keywords):
        return "high", "Task contains urgent or deadline-related keywords."

    if any(word in text for word in medium_keywords):
        return "medium", "Task seems important but not immediately critical."

    return "low", "No urgent keywords found, so priority is low."


@api_view(["GET", "POST"])
def task_list_create(request):
    global task_id_counter

    if request.method == "GET":
        return Response(tasks, status=status.HTTP_200_OK)

    if request.method == "POST":
        title = request.data.get("title")
        description = request.data.get("description", "")

        if not title or not title.strip():
            return Response(
                {"error": "Title is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        priority, reason = suggest_priority(title, description)

        new_task = {
            "id": task_id_counter,
            "title": title,
            "description": description,
            "status": "pending",
            "priority": priority,
            "priority_reason": reason
        }

        tasks.append(new_task)
        task_id_counter += 1

        return Response(new_task, status=status.HTTP_201_CREATED)


@api_view(["PATCH"])
def task_complete(request, task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "completed"
            return Response(task, status=status.HTTP_200_OK)

    return Response(
        {"error": "Task not found"},
        status=status.HTTP_404_NOT_FOUND
    )
