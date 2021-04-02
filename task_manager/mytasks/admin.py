from django.contrib import admin
from .models import Task, Comment, UserUs

admin.site.register(Task)
admin.site.register(Comment)
admin.site.register(UserUs)
