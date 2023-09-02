from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Event
# Create your views here.

@login_required(login_url='site_anb:login_path')
def index(request):
    return HttpResponse("Bem Vindo ao site da Água na Boca!")

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        user = User.objects.create_user(username, email,password)

        if user is not None:
            return  redirect('site_anb:login_path')

        else:
            messages.error(request, 'Não foi possível cadastrar o usuário.')
    return  render(request, 'site_anb/register_template.html')



def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('site_anb:index')

        else:
            messages.error(request, 'Apelido ou senha incorretos.')
    return render(request, 'site_anb/login_template.html')

@login_required(login_url='site_anb:login_path')
def new_event_view(request):
    if request.method == 'POST':
        user = request.user
        title = request.POST['title']
        place =request.POST['place']
        # date_time = request.POST['date_time']
        Event.objects.create(title=title, user=user, place=place)
        return redirect('site_anb:index')
    return render(request, 'site_anb/new_event_template.html')