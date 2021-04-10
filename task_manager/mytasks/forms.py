from django import forms
from mytasks.models import Task, Comment


class AddTaskForm(forms.Form):
    task_title = forms.CharField(max_length=100, label='Введите название задачи')
    task_text = forms.CharField(widget=forms.Textarea, max_length=100, label='Введите текст задачи')


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('task_title', 'task_text', "priority",)
        labels = {
            "task_title": "Название задачи",
            "task_text": "Текст задачи",
            "priority": ""
        }


class TaskExportForm(forms.Form):
    prio_high = forms.BooleanField(label="Высокий приоритет", initial=True, required=False)
    prio_med = forms.BooleanField(label="Средний приоритет", initial=True, required=False)
    prio_low = forms.BooleanField(label="Низкий приоритет", initial=True, required=False)


#
# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ('comment_to_task', 'comment_text', )
#
