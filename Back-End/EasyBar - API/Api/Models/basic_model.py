from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class Base(models.Model):
    criacao = models.DateTimeField(auto_now_add=True)
    atualizacao = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True