from django.urls import path
from .views import *

urlpatterns = [
    path('', todoItems, name='todoapp'),
    path('delete/<int:pk>/', deleteItem, name='delete')
]
