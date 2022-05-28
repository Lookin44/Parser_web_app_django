from django.forms import ModelForm, TextInput

from .models import BaseTask


class TaskForm(ModelForm):
    class Meta:
        model = BaseTask
        fields = ('domain_from',)
        widgets = {
            'domain_from': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://yandex.ru',
                'id': 'newTask'
            })
        }
