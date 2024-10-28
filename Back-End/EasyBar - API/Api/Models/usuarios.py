from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UsuarioManager(BaseUserManager):
    def create_user(self, nome, senha=None, **extra_fields):
        if not nome:
            raise ValueError("O campo nome deve ser preenchido")
        usuario = self.model(nome=nome, **extra_fields)
        usuario.set_password(senha)  # Hash da senha
        usuario.save(using=self._db)
        return usuario

    def create_superuser(self, nome, senha=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        return self.create_user(nome, senha, **extra_fields)


class Usuario(AbstractBaseUser):
    PAPEIS = [
        ('admin', 'Administrador'),
        ('funcionario', 'Funcionário'),
        ('gerente', 'Gerente'),
    ]
    
    nome = models.CharField(max_length=150, unique=True)
    cargo = models.CharField(max_length=50, choices=PAPEIS)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UsuarioManager()

    USERNAME_FIELD = 'nome'  
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.nome} ({self.cargo})"
