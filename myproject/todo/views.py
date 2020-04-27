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
        print(todos)
        context = {
            'todos':todos
        }
        print(context)
        return render(request,"todo/index.html",context)

def Delete(request, pk):
    todo = Todo.objects.get(id=pk)
    print(todo)

    if request.method == 'POST' :
        Todo.objects.filter(id=pk).delete()
        return redirect('/todo')
    # else:
    #     context = {'todo':todo}
    #     return render (request,'todo/delete.html',context)

def update(request,pk):
    todos = Todo.objects.get(id=pk)
    todo = []
    todo.append(todos)

    if (request.method == 'POST') :
        title = request.POST['title']
        text = request.POST['text']
        Todo.objects.filter(id=pk).update(title=title, text=text)   

        return redirect('/todo')
    else:
        context = {'todo':todo}
        print(context)
        return render(request,"todo/update.html",context)