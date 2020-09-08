from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.views import View
from django.views.generic import ListView
from mytasks.models import Task, Comment
from mytasks.forms import AddTaskForm, TaskForm
from django.views.generic.detail import DetailView


def index(request):
    return HttpResponse("Первый")


class TaskListView(ListView):
    queryset = Task.objects.all()
    context_object_name = "tasks"
    template_name = 'tasks/list.html'


class TaskCreateView(View):
    def my_render(self, request, form):
        return render(request, "tasks/task_creator.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return reverse("tasks:list")

        return self.my_render(request, form)

    def get(self, request, *args, **kwargs):
        form = TaskForm(request.POST)
        return self.my_render(request, form)


def add_task(request):
    if request.method == "POST":
        title = request.POST["task_title"]
        t = Task(task_title=title)
        t.save()
    return reverse("tasks:list")


def delete_task(request, uid):
    t = Task.objects.get(id=uid)
    t.delete()
    return reverse("tasks:list")


class TaskDetailView(DetailView):
    model = Task
    template_name = "tasks/detail.html"