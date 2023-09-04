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