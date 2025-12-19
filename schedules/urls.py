from django.urls import path
from .views import create_schedule, assign_schedule, my_schedule

urlpatterns = [
    path('create/', create_schedule, name='create_schedule'),
    path('assign/', assign_schedule, name='schedule_assign'),
    path('my/', my_schedule, name='my_schedule'),
]