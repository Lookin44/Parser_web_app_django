from django.urls import path
from . import views


urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('new_task/', views.new_task, name='new_task'),
    path('check_task/', views.check_task, name='check_task')
]
