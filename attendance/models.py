from django.db import models
from accounts.models import User

class Attendance(models.Model):
    STATUS_CHOICES = (
        ('Present', 'Present'),
        ('Absent', 'Absent'),
        ('Late', 'Late'),
        ('Half Day', 'Half Day'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    attendance_date = models.DateField()
    check_in = models.TimeField(null=True, blank=True)
    check_out = models.TimeField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Present')

    class Meta:
        unique_together = ('user', 'attendance_date')

    def __str__(self):
        return f"{self.user} - {self.attendance_date}"