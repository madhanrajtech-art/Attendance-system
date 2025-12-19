from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Leave


@login_required
def apply_leave(request):
    """
    Employee applies for leave
    """
    if request.method == 'POST':
        leave_date = request.POST.get('leave_date')
        leave_type = request.POST.get('leave_type')
        reason = request.POST.get('reason')

        Leave.objects.create(
            user=request.user,
            leave_date=leave_date,
            leave_type=leave_type,
            reason=reason
        )
        return redirect('leave_list')

    return render(request, 'apply.html')


@login_required
def leave_list(request):
    """
    Employee views own leave history
    """
    leaves = Leave.objects.filter(user=request.user).order_by('-leave_date')
    return render(request, 'leave_list.html', {'leaves': leaves})