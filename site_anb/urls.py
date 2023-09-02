from django.urls import path

from . import views

app_name = 'site_anb'
urlpatterns = [
    path("", views.index, name="index"),
    path('login/', views.login_view, name='login_path'),
    path('register/', views.register_view, name='register_path'),
    path('new_event/', views.new_event_view, name='new_event_path')
]