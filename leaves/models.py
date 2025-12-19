from django.db import models
from accounts.models import User

class Leave(models.Model):
    LEAVE_TYPE = (
        ('Casual', 'Casual'),
        ('Sick', 'Sick'),
        ('Paid', 'Paid'),
        ('Unpaid', 'Unpaid'),
    )

    STATUS = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    leave_date = models.DateField()
    leave_type = models.CharField(max_length=10, choices=LEAVE_TYPE)
    reason = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS, default='Pending')

    def __str__(self):
        return f"{self.user} - {self.leave_date}"
    


class Holiday(models.Model):
    holiday_date = models.DateField(unique=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description
    