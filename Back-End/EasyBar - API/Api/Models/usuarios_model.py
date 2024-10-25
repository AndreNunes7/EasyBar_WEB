from django.db import models

class Usuarios(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=150, unique=True)
    # email = models.EmailField(unique=True)
    cargo = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    # date_joined = models.DateTimeField(auto_now_add=True)  
    def __str__(self):
        return f'{self.username} - {self.cargo} - Ativo: {self.is_active} - Staff: {self.is_staff}'
