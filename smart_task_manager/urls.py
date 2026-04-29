from django.contrib import admin
from django.urls import path,include
from .views import task_list_create, task_complete

urlpatterns = [
    path("tasks", task_list_create, name="task-list-create"),
    path("tasks/<int:task_id>", task_complete, name="task-complete"),

    
]