from django.core.paginator import Paginator
from django.shortcuts import redirect, render

from .models import BaseTask, InformationFromDomain
from .forms import TaskForm
from .tasks import create_task


def main_page(request):
    all_info = InformationFromDomain.objects.all()
    paginator = Paginator(all_info, 50)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'index.html', context)


def new_task(request):
    form = TaskForm(request.POST)
    if form.is_valid():
        print(request.method)
        create_task.delay(form.data['domain_from'])
        form.save(commit=False)
        return redirect('check_task')
    return render(request, 'new_task.html', {'form': form})


def check_task(request):
    all_tasks = BaseTask.objects.all()
    paginator = Paginator(all_tasks, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'check_task.html', context)
