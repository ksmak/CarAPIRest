# Django
from django.contrib import admin

# Local
from .models import Task


admin.site.register(Task)
