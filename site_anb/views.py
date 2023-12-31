from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Event, Tento, UserProfile
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

def medical_survey_view(request):
    return render(request, 'site_anb/medical_survey_template.html')

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
        place = request.POST['place']
        date_time = request.POST['date_time']
        Event.objects.create(title=title, user=user, place=place, date_time=date_time)
        return redirect('site_anb:event_list_path')
    return render(request, 'site_anb/new_event_template.html')

@login_required(login_url='site_anb:login_path')
def event_list_view(request):
    event_list = Event.objects.order_by('date_time')
    return render(request, 'site_anb/event_list_template.html', {'event_list': event_list})

@login_required(login_url='site_anb:login_path')
def event_detail_view(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'site_anb/event_detail_template.html', {'event': event})

@login_required(login_url='site_anb:login_path')
def remove_event_view(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    event.delete()
    return redirect('site_anb:event_list_path')

hierarchy_filter = [
    'Moradora',
    'Agregada',
    'Pseudo-morador',
    'Bixo',
]

@login_required(login_url='site_anb:login_path')
def new_tento_view(request):
    user_profile_list = UserProfile.objects.filter(hierarchy__in=hierarchy_filter)

    if request.method == 'POST':
        description = request.POST['description']
        nickname = request.POST['nickname']
        to_user = user_profile_list.get(nickname=nickname)
        from_user = user_profile_list.get(nickname=request.user.username)
        to_user.tentos += 1
        to_user.save()
        Tento.objects.create(from_user=from_user, to_user=to_user, description=description)
    return render(request, 'site_anb/new_tento_template.html', {'user_profile_list': user_profile_list})

@login_required(login_url='site_anb:login_path')
def tento_list_view(request):
    tento_list = Tento.objects.all()
    return render(request, 'site_anb/tento_list_template.html', {'tento_list': tento_list})
