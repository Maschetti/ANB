from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
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
            return redirect('anb_site:index')

        else:
            messages.error(request, 'Apelido ou senha incorretos.')
    return render(request, 'site_anb/login_template.html')
