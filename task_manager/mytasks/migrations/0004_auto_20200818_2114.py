# Generated by Django 3.1 on 2020-08-18 18:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mytasks', '0003_auto_20200818_2109'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='task',
            new_name='comment_to_task',
        ),
    ]
