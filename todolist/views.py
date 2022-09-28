from urllib import request
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from todolist.forms import taskForm
from todolist.models import Task
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
...
# Create your views here.
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data_todolist = Task.objects.filter(user=request.user)
    context = {
        'list_todolist': data_todolist,
        'nama': 'Fathan Hadyan',
        'last_login': request.COOKIES['last_login'],
    }
    return render(request, "todolist.html", context)


def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("todolist:show_todolist"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

def create_task(request):
    form = taskForm()

    if request.method == "POST":
        form = taskForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.user = request.user
            var.save()
            return redirect('todolist:show_todolist')
    
    context = {'form':form}
    return render(request, 'create-task.html', context)
    
def update_task(request, id):
    todo = Task.objects.get(id = id)
    todo.is_finished = not(todo.is_finished)
    todo.save()
    return redirect('todolist:show_todolist')


def delete_task(request, id):
    todo = Task.objects.get(id = id)
    todo.delete()
    return redirect('todolist:show_todolist')