from django import forms
from mytasks.models import Task


class AddTaskForm(forms.Form):
    task_title = forms.CharField(max_length=100, label='Введите название задачи')
    task_text = forms.CharField(widget=forms.Textarea, max_length=100, label='Введите текст задачи')


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('task_title', 'task_text', )
