from django.contrib import admin

# Register your models here.
from .models import TodoNote

admin.site.register(TodoNote)