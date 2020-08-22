from django.shortcuts import render, redirect
from django.http import HttpResponse
from mytasks.models import Task, Comment
from mytasks.forms import AddTaskForm, TaskForm


def index(request):
    return HttpResponse("Первый")


def tasks_list(request):
    all_task = Task.objects.all()
    return render(
        request,
        'tasks/list.html',
        {
            'tasks': all_task,
        }
    )


def task_creator(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/mytasks/list")
    else:
        form = TaskForm()

    return render(request, "tasks/task_creator.html", {"form": form})


def add_task(request):
    if request.method == "POST":
        title = request.POST["task_title"]
        t = Task(task_title=title)
        t.save()
    return redirect("/mytasks/list/")
