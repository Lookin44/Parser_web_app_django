from django.core.exceptions import ValidationError
from django.forms import ModelForm, URLInput

from .models import BaseTask


class TaskForm(ModelForm):

    def clean_url(self):
        url = self.cleaned_data['domain_from']
        if url.startswith('http://') or url.startswith('https://'):
            return url
        else:
            raise ValidationError(
                'URL address must start with http:// or https://'
            )

    class Meta:
        model = BaseTask
        fields = ('domain_from',)
        error_messages = {
            'invalid': 'URL address must start with http:// or https://',
            'required': 'Give URL address '
        }
        widgets = {
            'domain_from': URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://address.com or http://address.com',
                'id': 'newTask'
            })
        }
