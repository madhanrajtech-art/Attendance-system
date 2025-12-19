from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from .models import WorkSchedule, EmployeeSchedule
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()


# -------------------------------
# Admin: Create Work Schedule
# -------------------------------
@permission_required('schedules.add_workschedule', raise_exception=True)
def create_schedule(request):
    if request.method == 'POST':
        shift_name = request.POST.get('shift_name')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        working_days = request.POST.get('working_days')

        WorkSchedule.objects.create(
            shift_name=shift_name,
            start_time=start_time,
            end_time=end_time,
            working_days=working_days
        )
        return redirect('schedule_list')

    return render(request, 'create.html')


# -------------------------------
# Admin: Assign Schedule to User
# -------------------------------
@permission_required('schedules.add_employeeschedule', raise_exception=True)
def assign_schedule(request):
    users = User.objects.filter(is_staff=False)
    schedules = WorkSchedule.objects.all()

    if request.method == 'POST':
        user_id = request.POST.get('user')
        schedule_id = request.POST.get('schedule')
        assigned_date = request.POST.get('assigned_date')

        EmployeeSchedule.objects.create(
            user_id=user_id,
            schedule_id=schedule_id,
            assigned_date=assigned_date
        )
        return redirect('schedule_assign')

    return render(
        request,
        'assign.html',
        {'users': users, 'schedules': schedules}
    )


# -------------------------------
# Employee: View Own Schedule
# -------------------------------
@login_required
def my_schedule(request):
    schedules = EmployeeSchedule.objects.filter(user=request.user)
    return render(
        request,
        'my_schedule.html',
        {'schedules': schedules}
    )