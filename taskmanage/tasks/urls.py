from django.urls import path
from .views import TaskList,TaskUpdate

urlpatterns = [
    path('tasks/', TaskList.as_view(), name='task-list'),
    path('tasks/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
]