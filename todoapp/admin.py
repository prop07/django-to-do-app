from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(TodoApp)
class TodoApp(admin.ModelAdmin):
    list_display=['title', 'description']