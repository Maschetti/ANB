from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Emergency_contact:
    name = models.CharField(max_length=100, verbose_name="Nome do contato de emergência")
    telephone_number = models.CharField(max_length=50, verbose_name="Telefone do contato de emergência")

class Address(models.Model):
    street = models.CharField(max_length=100, verbose_name="Rua")
    district = models.CharField(max_length=100, verbose_name="Bairro")
    number = models.CharField(max_length=10, verbose_name="Número")
    complement = models.CharField(max_length=50, verbose_name="complemento", blank=True, null=True)

class Event(models.Model):
    title =models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    place = models.CharField(max_length=50)
    date_time = models.DateTimeField()

    def __str__(self):
        return  self.title
    
class Medical_PDF(models.model):
    BLOOD_TYPE_CHOICES = (
            ('A+', 'A+'),
            ('A-', 'A-'),
            ('B+', 'B+'),
            ('B-', 'B-'),
            ('AB+', 'AB+'),
            ('AB-', 'AB-'),
            ('O+', 'O+'),
            ('O-', 'O-'),
        )
    full_name = models.CharField(max_length=100, verbose_name="nome completo")
    birthday = models.DateField(verbose_name="Data de Aniversário")
    cpf = models.CharField(max_length=12, verbose_name="CPF")
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    cellphone_number =  models.CharField(max_length=30, verbose_name="Celular")
    emergency_contact = models.ForeignKey(Emergency_contact, on_delete=models.CASCADE)
    blood_type = models.CharField(max_length=3, choices=BLOOD_TYPE_CHOICES)
    regular_medicines = models.CharField(max_length=100, blank=True, null=True, default='Nenhum')
    past_medicines = models.CharField(max_length=100, blank=True, null=True, default='Nenhum')
    broken_bones = models.CharField(max_length=100, blank=True, null=True, default='Nenhum')
    alergies = models.CharField(max_length=100, blank=True, null=True, default='Nenhum')
    info = models.TextField(blank=True, null=True)
    vaccination = models.ImageField()

    


    
