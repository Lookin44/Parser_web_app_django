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
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            create_task.delay(form.cleaned_data['domain_from'])
            return redirect('check_task')
        context = {
            'form': form,
            'error': form.errors
        }
        return render(request, 'new_task.html', context)
    return render(request, 'new_task.html', {'form': TaskForm()})


def check_task(request):
    all_tasks = BaseTask.objects.all()
    context = {
        'all_tasks': all_tasks,
    }
    return render(request, 'check_task.html', context)

