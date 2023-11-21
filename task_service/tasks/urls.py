from django.urls import path
from .views import TaskView

urlpatterns = [
    path('task/<int:task_id>/', TaskView.as_view(), name='task_detail'),
    path('task/', TaskView.as_view(), name='create_task'),
]
