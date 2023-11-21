from django.contrib import admin

# Register your models here.
from .models import Task

Models = [Task]
for model in Models:
    admin.site.register(model)