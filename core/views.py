from django.shortcuts import render, redirect, get_object_or_404
from .forms import TaskForm
from .models import TaskModel
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# --------------------------- CRUD --------------------------- #

@login_required(login_url="/core/accounts/login/")
def home(request):
    dados = TaskModel.objects.filter(user=request.user.id)
    contexto = {
        "titulo": "Lucas",
        "dados": dados
    }
    return render (request, 'home.html', contexto)

@login_required(login_url="/core/accounts/login/")
def addTask(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('home')
    contexto = {
        "form":form
    }
    return render(request, 'form.html', contexto)

@login_required(login_url="/core/accounts/login/")
def updateTask(request, pk):
    dados = get_object_or_404(TaskModel, pk=pk, user=request.user)
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

@login_required(login_url="/core/accounts/login/")
def deleteTask(request, pk):
    dados = get_object_or_404(TaskModel, pk=pk, user=request.user)
    dados.delete()
    return redirect('home')

@login_required(login_url="/core/accounts/login/")
def checkboxTask(request, pk):
    dados = get_object_or_404(TaskModel, pk=pk, user=request.user)
    dados.concluido = not dados.concluido
    dados.save()
    return redirect('home')

# --------------------------- CRUD --------------------------- #

# --------------------------- AUTH --------------------------- #


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Nome de usuário ou senha inválidos'})
            
    return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username'].strip()
        email = request.POST['email'].strip()
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']

        if not username or not email or not password or not password_confirm:
            return render(request, 'register.html', {'error': 'Todos os campos são obrigatórios'})
        
        if password_confirm == password:
            try:
                user = User.objects.create_user(username=username, email=email, password=password)
                return redirect('login')
            except:
                return render(request, 'register.html', {'error': 'Este nome de usuário já está em uso.'})
        else:
            return render(request, 'register.html', {'error': 'As senhas não coincidem'})
    
    return render(request, 'register.html')

@login_required(login_url="/core/accounts/login/")
def logout_view(request):
    logout(request)
    return redirect('login')