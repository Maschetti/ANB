from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Event(models.Model):
    title =models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    place = models.CharField(max_length=50)
    date_time = models.DateTimeField()

    def __str__(self):
        return  self.title
