from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import TodoApp

# Create your views here.
def todoItems(request):
    todoItems = TodoApp.objects.all()
    context={'todoItems':todoItems}
    if request.method == "POST" and (request.POST['title']!='' or request.POST['description']!=''):
        TodoApp(title=request.POST['title'], description=request.POST['description']).save()
        # TodoApp.objects.create(title=request.POST['title'], description=request.POST['description'])
    return render(request, 'todoapp/index.html', context)
    
def deleteItem(request, pk):
    todoItem= TodoApp.objects.get(id=pk)
    todoItem.delete()
    return HttpResponseRedirect("/")
