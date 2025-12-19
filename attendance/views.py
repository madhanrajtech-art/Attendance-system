from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Attendance

@login_required
def mark_attendance(request):
    today = timezone.now().date()

    attendance, created = Attendance.objects.get_or_create(
        user=request.user,
        attendance_date=today
    )

    if request.method == 'POST':
        if not attendance.check_in:
            attendance.check_in = timezone.now().time()
        else:
            attendance.check_out = timezone.now().time()

        attendance.save()
        return redirect('dashboard')

    return render(request, 'mark.html', {'attendance': attendance})



from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')