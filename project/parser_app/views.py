from django.shortcuts import redirect, render

from .models import BaseTask, InformationFromDomain
from .forms import TaskForm
from .tasks import create_task


def main_page(request):
    all_info = InformationFromDomain.objects.all()
    context = {
        'all_info': all_info,
    }
    return render(request, 'index.html', context)


def new_task(request):
    form = TaskForm(request.POST)
    if form.is_valid():
        create_task.delay(form.data['domain_from'])
        form.save(commit=False)
        return redirect('check_task')
    return render(request, 'new_task.html', {'form': form})


def check_task(request):
    all_tasks = BaseTask.objects.all()
    context = {
        'all_tasks': all_tasks,
    }
    return render(request, 'check_task.html', context)
