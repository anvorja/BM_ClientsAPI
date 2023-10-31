from datetime import datetime

from django.db import models
from django.contrib.auth.models import User


class Client(models.Model):
    nombre = models.CharField(max_length=40)
    nit = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    prioritario = models.BooleanField(default=False)
    descripcion = models.CharField(max_length=60)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre + ' - ' + self.user.username

