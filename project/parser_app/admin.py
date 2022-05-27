from django.contrib import admin

from .models import BaseTask, InformationFromDomain


@admin.register(BaseTask)
class BaseTaskAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name_from_celery',
        'is_success',
        'created_at',
        'updated_at'
    ]
    readonly_fields = ['created_at']
    list_filter = ['is_success']


@admin.register(InformationFromDomain)
class InformationFromDomainAdmin(admin.ModelAdmin):
    list_display = ['task_name', 'domain', 'country']
