from django.contrib import admin

# Register your models here.
from .models import User

Models = [User]
for model in Models:
    admin.site.register(model)