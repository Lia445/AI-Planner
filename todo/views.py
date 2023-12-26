from .models import Task
from .forms import TaskForm
from datetime import datetime, timedelta
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants
from django.shortcuts import render, redirect



def register(request):
    if request.user.is_authenticated:
        return redirect('/index')
    if request.method == "GET":
        return render(request, 'register.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        if username in (user.username for user in User.objects.all()):
            messages.add_message(request, constants.ERROR, 'Username already in use')
            return redirect('/register')
        password = request.POST.get('password1')
        if password != request.POST.get('password2'):
            messages.add_message(request, constants.ERROR, 'Passwords need to match')
            return redirect('/register')
        user = User.objects.create_user(username=username, password=password)
        user.save()
        login(request, user)
        return redirect('/login')
        

def login_view(request):
    if request.user.is_authenticated:
        return redirect('/index')
    if request.method == "GET":
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})
    elif request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
        
         
def logout_view(request):
    logout(request)
    return redirect('/login')            


@login_required
def index(request):
    all_tasks = Task.objects.filter(user=request.user).order_by("date")
    today = all_tasks.filter(date=datetime.now()).order_by("date")
    this_week = all_tasks.filter(date__range=(datetime.now(), datetime.now() + timedelta(days=7))).order_by("date")
    return render(request, 'index.html', {'today': today, 'this_week': this_week, 'all_tasks': all_tasks})
    

@login_required
def create(request):
    if request.method == "GET":
        form = TaskForm()
        return render(request, 'create.html', {'form': form}) 
    elif request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = Task(
                user=request.user,
                title=form.cleaned_data.get('title'),
                description=form.cleaned_data.get('description'),
                date=form.cleaned_data.get('date'),
                hours=form.cleaned_data.get('hours')
            )
            task.save()
            messages.add_message(request, constants.SUCCESS, 'Task created successfully')
            return redirect('/index')
    

@login_required
def view_task(request, id):
    task = Task.objects.get(id=id)
    return render(request, 'view_task.html', {'task': task})


@login_required    
def update(request, id):
    task = Task.objects.get(id=id)
    if request.method == "GET":
        form = TaskForm(instance=task)
        return render(request, 'update.html', {'task': task, 'form': form}) 
    elif request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.add_message(request, constants.SUCCESS, 'Task updated successfully')
            return redirect('/index') 
        
        
@login_required
def next_status(request, id):
    task = Task.objects.get(id=id)
    if task.status == 'NOT STARTED':
        task.status = 'DOING'
    elif task.status == 'DOING':
        task.status = 'DONE'
    task.save()
    return redirect('/index')


@login_required
def delete(request, id):
    task = Task.objects.get(id=id)
    if request.method == "GET":
        return render(request, 'delete.html', {'task': task}) 
    elif request.method == "POST":
        task.delete()
        messages.add_message(request, constants.SUCCESS, 'Task deleted successfully')
        return redirect('/index')


