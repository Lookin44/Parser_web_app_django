from django.forms import ModelForm, Textarea

from .models import BaseTask


class TaskForm(ModelForm):
    class Meta:
        model = BaseTask
        fields = ('domain_from',)
        # widgets = {
        #     'domain_from': Textarea(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'https://yandex.ru',
        #         'id': 'newTask'
        #     })
        # }
