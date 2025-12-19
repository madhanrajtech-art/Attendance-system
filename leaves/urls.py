from django.urls import path
from .views import apply_leave, leave_list

urlpatterns = [
    path('apply/', apply_leave, name='apply_leave'),
    path('list/', leave_list, name='leave_list'),
]