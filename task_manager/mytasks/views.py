from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.views import View
from django.views.generic import ListView
# from mytasks.models import Task
from .models import Task
# from mytasks.forms import AddTaskForm, TaskForm
from .forms import AddTaskForm, TaskForm
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


@login_required
def index(request):
    return HttpResponse("Первый")


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = "tasks"
    template_name = 'tasks/list.html'

    def get_queryset(self):
        u = self.request.user
        return u.tasks.all()

        # Тут должно быть:
        # u = User.objects.get(id=1)
        # Task.objects.filter(owner=u.id)


# class TaskCommentView(DetailView):
#     model = Comment
#     context_object_name = "comments"
#     template_name = 'tasks/detail.html'


class TaskCreateView(View):
    def my_render(self, request, form):
        return render(request, "tasks/task_creator.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = TaskForm(request.POST)
        if form.is_valid():
            new_task = form.save(commit=False)
            new_task.owner = request.user
            new_task.save()
            return redirect(reverse("tasks:list"))

        return render(request, "tasks/task_creator.html", {"form": form})

    def get(self, request, *args, **kwargs):
        form = TaskForm()
        return render(request, "tasks/task_creator.html", {"form": form})


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
