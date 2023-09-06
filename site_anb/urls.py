from django.urls import path

from . import views

app_name = 'site_anb'
urlpatterns = [
    path("", views.index, name="index"),
    path('login/', views.login_view, name='login_path'),
    path('register/', views.register_view, name='register_path'),
    path('medical_survey/', views.medical_survey_view, name='medical_survey_path'),

    path('new_event/', views.new_event_view, name='new_event_path'),
    path('event_list/', views.event_list_view, name='event_list_path'),
    path('event_detail/<int:event_id>/', views.event_detail_view, name='event_detail_path'),
    path('remove_event/<int:event_id>/', views.remove_event_view, name='remove_event_path'),

    path('new_tento/', views.new_tento_view, name='new_tento_path'),
    path('tento_list/', views.tento_list_view, name='tento_list_path'),
]
