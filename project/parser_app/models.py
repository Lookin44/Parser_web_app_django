from django.db import models


class BaseTask(models.Model):
    """Статус задачи переданной Celery"""
    name_from_celery = models.CharField(max_length=100)
    domain_from = models.URLField(max_length=100)
    is_success = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name_from_celery

    class Meta:
        ordering = ('-created_at', )


class InformationFromDomain(models.Model):
    """Информация по доменам с API Вomainsdb"""
    task_name = models.ForeignKey(
        BaseTask,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='results'
    )
    domain = models.URLField(max_length=500)
    create_date = models.DateTimeField()
    update_date = models.DateTimeField()
    country = models.CharField(max_length=100, null=True)
    is_dead = models.BooleanField()
    a = models.CharField(max_length=1000, null=True)
    ns = models.CharField(max_length=1000, null=True)
    cname = models.CharField(max_length=1000, null=True)
    mx = models.CharField(max_length=1000, null=True)
    txt = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.domain

    class Meta:
        ordering = ('pk',)
