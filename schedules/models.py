from django.db import models
from accounts.models import User

class WorkSchedule(models.Model):
    shift_name = models.CharField(max_length=50)
    start_time = models.TimeField()
    end_time = models.TimeField()
    working_days = models.CharField(max_length=50)

    def __str__(self):
        return self.shift_name


class EmployeeSchedule(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    schedule = models.ForeignKey(WorkSchedule, on_delete=models.CASCADE)
    assigned_date = models.DateField()

    def __str__(self):
        return f"{self.user} - {self.schedule}"