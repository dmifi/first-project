# Generated by Django 3.1 on 2020-08-18 16:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_title', models.CharField(max_length=100, verbose_name='Название задачи')),
                ('task_text', models.TextField(verbose_name='Текст задачи')),
                ('pub_date', models.DateTimeField(verbose_name='Дата постановки задачи')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=100, verbose_name='Имя комментатора')),
                ('first_name', models.CharField(max_length=100, verbose_name='Имя комментатора')),
                ('second_name', models.CharField(max_length=100, verbose_name='Имя комментатора')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.CharField(max_length=200, verbose_name='Текст комментария')),
                ('nickname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mytasks.user')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mytasks.task')),
            ],
        ),
    ]
