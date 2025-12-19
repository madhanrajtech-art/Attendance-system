from django.urls import path
from .views import task_list, update_task_status

urlpatterns = [
    path('', task_list, name='task_list'),
    path('update/<int:task_id>/', update_task_status, name='update_task'),
]