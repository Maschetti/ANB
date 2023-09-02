from django.urls import path

from . import views

app_name = 'site_anb'
urlpatterns = [
    path("", views.index, name="index"),
    path('login/', views.login_view, name='login_path'),
    path('regiseter/', views.register_view, name='register_path')
]