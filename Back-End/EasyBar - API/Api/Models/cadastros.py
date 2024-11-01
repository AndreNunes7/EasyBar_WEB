from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password
from django.utils.translation import gettext_lazy as _
from ..Auth.validators import UnicodeUsernameValidator
from ..Auth import valida_password

class Cadastro(models.Model):
    class Meta:
        verbose_name = _("usuário")
        verbose_name_plural = _("usuários")
        
        permissions = [
            ("custom_view_user", "Can view user"),
            ("custom_add_user", "Can add user"),
            ("custom_change_user", "Can change user"),
            ("custom_delete_user", "Can delete user"),
        ]

    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _("Nome"),
        max_length=150,
        unique=True,
        help_text=_("Obrigatório. 150 caracteres ou menos. Apenas letras, dígitos e os caracteres @/./+/-/_."), 
        validators=[username_validator],
        error_messages={
            "unique": _("Um usuário com este nome já existe."),
        },
    )
    
    password = models.CharField(_("Senha"), max_length=128)
    
    PAPEIS = [
        ('admin', 'Administrador'),
        ('funcionario', 'Funcionário'),
        ('gerente', 'Gerente'),
    ]

    papel = models.CharField(
        _("Papel"),
        max_length=50,
        choices=PAPEIS,
        default='funcionario'
    )
    
    cargo = models.CharField(
        _("Cargo"),
        max_length=50,
        blank=True,
        null=False
    )

    telefone = models.CharField(
        _("Telefone"),
        max_length=15,
        blank=True,
        null=True
    )
    
    is_staff = models.BooleanField(
        _("Status admin"),
        default=False,
        help_text=_("Indica se o usuário pode acessar o site administrativo."),
    )
    
    is_active = models.BooleanField(
        _("Ativo"),
        default=True,
        help_text=_("Indica se este usuário deve ser tratado como ativo. Desmarque em vez de deletar contas."),
    )

    is_superuser = models.BooleanField(
        _("Superusuário"),
        default=False,
        help_text=_("Indica se este usuário tem permissões de superusuário."),
    )

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['cargo']

    def clean(self):
        super().clean()
        
        if self.password:
            try:
                valida_password(self.password, username=self.username)
            except ValidationError as e:
                raise ValidationError({'password': e.messages})

    def save(self, *args, **kwargs):
        self.full_clean()
        
        if self.password and not self.password.startswith('pbkdf2_sha256$'):
            self.password = make_password(self.password)

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.username} ({self.get_papel_display()})"
