from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import TaskModel

def home(request):
    dados = TaskModel.objects.all()
    contexto = {
        "titulo": "Lucas",
        "dados": dados
    }
    return render (request, 'home.html', contexto)

def addTask(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    contexto = {
        "form":form
    }
    return render(request, 'form.html', contexto)

def updateTask(request, pk):
    dados = TaskModel.objects.get(pk=pk)
    form = TaskForm(instance=dados)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=dados)
        if form.is_valid():
            form.save()
            return redirect('home')
    contexto = {
        "form":form
    }
    return render(request, 'form.html', contexto)

def deleteTask(request, pk):
    dados = TaskModel.objects.get(pk=pk)
    dados.delete()
    return redirect('home')