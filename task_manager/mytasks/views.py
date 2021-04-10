from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.db.models import Q
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.views import View
from django.views.generic import ListView
# from mytasks.models import Task
from .models import Task
# from mytasks.forms import AddTaskForm, TaskForm
from .forms import AddTaskForm, TaskForm, TaskExportForm
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


class TaskEditView(View):
    def post(self, request, pk, *args, **kwargs):
        t = Task.objects.get(id=pk)
        form = TaskForm(request.POST, instance=t)
        if form.is_valid():
            new_task = form.save(commit=False)
            new_task.owner = request.user
            new_task.save()
            return redirect(reverse("tasks:list"))

        return render(request, "tasks/edit.html", {"form": form, "task": t})

    def get(self, request, pk, *args, **kwargs):
        t = Task.objects.get(id=pk)
        form = TaskForm(instance=t)
        return render(request, "tasks/edit.html", {"form": form, "task": t})


class TaskExportView(LoginRequiredMixin, View):
    def generate_body(self, user, priorities):
        q = Q()
        if priorities["prio_high"]:
            q = q | Q(priority=Task.PRIORITY_HIGH)
        if priorities["prio_med"]:
            q = q | Q(priority=Task.PRIORITY_MEDIUM)
        if priorities["prio_low"]:
            q = q | Q(priority=Task.PRIORITY_LOW)
        tasks = Task.objects.filter(owner=user).filter(q).all()

        body = "Ваши задачи и их приоритеты:\n"
        for t in list(tasks):
            if t.is_completed:
                body += f"[x] {t.task_text} ({t.get_priority_display()})\n"
            else:
                body += f"[ ] {t.task_text} ({t.get_priority_display()}) \n"
        return body

    def post(self, request, *args, **kwargs):
        form = TaskExportForm(request.POST)
        if form.is_valid():
            email = request.user.email
            body = self.generate_body(request.user, form.cleaned_data)
            send_mail("Задачи", body, settings.EMAIL_HOST_USER, [email])
            messages.success(request, "Задачи были отправлены на электронную почту %s" % email)
        else:
            messages.error(request, "Возникла ошибка, попробуйте еще раз")
        return redirect(reverse("tasks:list"))

    def get(self, request, *args, **kwargs):
        form = TaskExportForm()
        return render(request, "tasks/export.html", {"form": form})


def add_task(request):
    if request.method == "POST":
        title = request.POST["task_title"]
        t = Task(task_title=title)
        t.save()
    return reverse("tasks:list")


def delete_task(request, uid):
    t = Task.objects.get(id=uid)
    t.delete()
    messages.success(request, "Задача удалена")
    return redirect(reverse("tasks:list"))


def complete_task(request, uid):
    t = Task.objects.get(id=uid)
    t.is_completed = True
    t.save()
    return HttpResponse("OK")


class TaskDetailView(DetailView):
    model = Task
    template_name = "tasks/detail.html"
