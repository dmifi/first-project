from django.urls import path

from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.TaskListView.as_view(), name='list'),
    path('create/', views.TaskCreateView.as_view(), name='task_creator'),
    path('add-task/', views.add_task, name="api-add-task"),
    path('detail/<int:pk>', views.TaskDetailView.as_view(), name="detail"),
]
