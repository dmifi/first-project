from django.db import models


# Create your models here.

class User(models.Model):
    nickname = models.CharField('Имя комментатора', max_length=100)
    first_name = models.CharField('Имя комментатора', max_length=100)
    second_name = models.CharField('Имя комментатора', max_length=100)


class Task(models.Model):
    task_title = models.CharField('Название задачи', max_length=100)
    task_text = models.TextField('Текст задачи')
    pub_date = models.DateTimeField('Дата постановки задачи')


class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    comment_text = models.CharField('Текст комментария', max_length=200)
    nickname = models.ForeignKey(User, on_delete=models.CASCADE)
