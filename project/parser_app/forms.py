from django.forms import ModelForm

from .models import BaseTask


class TaskForm(ModelForm):
    class Meta:
        model = BaseTask
        fields = ('domain_from',)
