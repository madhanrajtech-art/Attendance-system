from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from .models import Task

@login_required
def task_list(request):
    tasks = Task.objects.filter(assigned_to=request.user)
    return render(request, 'list.html', {'tasks': tasks})


@permission_required('tasks.change_task', raise_exception=True)
def update_task_status(request, task_id):
    task = Task.objects.get(id=task_id)

    if request.method == 'POST':
        task.status = request.POST.get('status')
        task.save()
        return redirect('task_list')

    return render(request, 'update.html', {'task': task})