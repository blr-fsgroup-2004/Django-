from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Todo
from .forms import *
# Create your views here.

def index(request):
    todos = Todo.objects.all()

    form = TodoForm()

    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            text = form.cleaned_data['text']
            obj=Todo(title=title,text=text)
            obj.save()
            return redirect('/todo')
        
    context = {'todos':todos,'form':form}
    return render(request ,'todo/index.html',context)


# def Delete(request, pk):
#     todo = Todo.objects.get(id=pk)
#     print(todo)

#     if request.method == 'POST' :
#         Todo.objects.filter(id=pk).delete()
#         return redirect('/todo')
    # else:
    #     context = {'todo':todo}
    #     return render (request,'todo/delete.html',context)

# def update(request,pk):
#     todos = Todo.objects.get(id=pk)
#     todo = []
#     todo.append(todos)

#     if (request.method == 'POST') :
#         title = request.POST['title']
#         text = request.POST['text']
#         Todo.objects.filter(id=pk).update(title=title, text=text)   

#         return redirect('/todo')
#     else:
#         context = {'todo':todo}
#         print(context)
#         return render(request,"todo/update.html",context)