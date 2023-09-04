from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    place = models.CharField(max_length=50)
    date_time = models.DateTimeField()

    def __str__(self):
        return  self.title

HIERARCHY_CHOICES = [
    ('Ex-aluna', 'Ex-aluna'),
    ('Homenageado', 'Homenageado'),
    ('Homenageada', 'Homenageada'),
    ('Moradora', 'Moradora'),
    ('Agregada', 'Agregada'),
    ('Pseudo-morador', 'Pseudo-morador'),
    ('Bixo', 'Bixo')
]

class UserProfile(models.Model):
    nickname = models.CharField(max_length=100)
    hierarchy = models.CharField(max_length=15, choices=HIERARCHY_CHOICES)
    course = models.CharField(max_length=100, default='')
    tentos = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nickname

class Tento(models.Model):
    from_user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=True, null=True, related_name='giver')
    to_user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=True, null=True, related_name='receiver')
    description = models.CharField(max_length=200)
    date_time = models.DateTimeField()

    def __str__(self):
        return self.description

class EmergencyContact(models.Model):
    name = models.CharField(max_length=100)
    telephone_number = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Address(models.Model):
    street = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    number = models.CharField(max_length=10)
    complement = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.street
#
# BLOOD_TYPE_CHOICES = [
#     ('A+', 'A+'),
#     ('A-', 'A-'),
#     ('B+', 'B+'),
#     ('B-', 'B-'),
#     ('AB+', 'AB+'),
#     ('AB-', 'AB-'),
#     ('O+', 'O+'),
#     ('O-', 'O-'),
# ]
#
# class MedicalPDF(models.Model):
#     full_name = models.CharField(max_length=100, verbose_name="nome completo")
#     birthday = models.DateField(verbose_name="Data de Aniversário")
#     cpf = models.CharField(max_length=12, verbose_name="CPF")
#     address = models.ForeignKey(Address, on_delete=models.CASCADE)
#     cellphone_number = models.CharField(max_length=30, verbose_name="Celular")
#     emergency_contact = models.ForeignKey(EmergencyContact, on_delete=models.CASCADE)
#     blood_type = models.CharField(max_length=3, choices=BLOOD_TYPE_CHOICES)
#     regular_medicines = models.CharField(max_length=100, blank=True, null=True, default='Nenhum')
#     past_medicines = models.CharField(max_length=100, blank=True, null=True, default='Nenhum')
#     broken_bones = models.CharField(max_length=100, blank=True, null=True, default='Nenhum')
#     allergies = models.CharField(max_length=100, blank=True, null=True, default='Nenhum')
#     info = models.TextField(blank=True, null=True)
#
#     def __str__(self):
#         return  self.full_name
