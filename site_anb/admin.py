from django.contrib import admin
from .models import Event, UserProfile, Tento, EmergencyContact, Address, MedicalPDF

# Register your models here.
admin.site.register(Event)
admin.site.register(UserProfile)
admin.site.register(Tento)
admin.site.register(EmergencyContact)
admin.site.register(Address)
admin.site.register(MedicalPDF)
