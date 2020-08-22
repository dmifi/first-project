from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.tasks_list, name='list'),
    path('create/', views.task_creator, name='task_creator'),
    path('add-task/', views.add_task, name="api-add-task"),
]
