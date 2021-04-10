import datetime
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.

class UserUs(models.Model):
    nickname = models.CharField('Никнейм', max_length=100)
    first_name = models.CharField('Имя', max_length=100)
    last_name = models.CharField('Фамилия', max_length=100)

    def __str__(self):
        return self.pk


class Task(models.Model):
    PRIORITY_HIGH = 1
    PRIORITY_MEDIUM = 2
    PRIORITY_LOW = 3

    PRIORITY_CHOICES = [
        (PRIORITY_HIGH, "Высокий приоритет"),
        (PRIORITY_MEDIUM, "Средний приоритет"),
        (PRIORITY_LOW, "Низкий приоритет"),
    ]

    task_title = models.CharField('Название задачи', max_length=100)
    task_text = models.TextField('Текст задачи')
    is_completed = models.BooleanField("Выполнено", default=False)
    created = models.DateTimeField('Дата постановки задачи', auto_now_add=True)
    updated = models.DateTimeField('Обновлено', auto_now=True)
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='tasks')
    priority = models.IntegerField(
        "Приоритет", choices=PRIORITY_CHOICES, default=PRIORITY_MEDIUM
    )

    def __str__(self):
        return self.task_title

    # def today_task(self):
    #     return self.created >= (timezone.now() - datetime.timedelta(days=1))

    class Meta:
        ordering = ('-created',)


class Comment(models.Model):
    nickname = models.ForeignKey(
        User,
        verbose_name="Никнейм",
        on_delete=models.CASCADE)
    comment_to_task = models.ForeignKey(Task, verbose_name="Задача", on_delete=models.CASCADE)
    comment_text = models.CharField('Текст комментария', max_length=200)

    def __str__(self):
        return self.comment_text


