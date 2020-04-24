from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Todo
# Create your views here.

def index(request):
    if(request.method == 'POST'):
        title = request.POST['title']
        text = request.POST['text']

        todo = Todo(title=title, text=text)
        todo.save()

        return redirect('/todo')
    else:
        todos = Todo.objects.all()
        context = {
            'todos':todos
        }
        return render(request,"todo/index.html",context)