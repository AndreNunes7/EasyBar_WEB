import re
from django.core.exceptions import ValidationError
from django.core import validators
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.hashers import make_password
import string



# Username: 
@deconstructible
class ASCIIUsernameValidator(validators.RegexValidator):
    regex = r"^[\w.@+-]+\Z"
    message = _(
        "Insira um nome de usuário válido. Este valor pode conter apenas letras minúsculas a-z sem acento, \
            letras maiúsculas A-Z, números e os caracteres @/./+/-/_."
    )
    flags = re.ASCII


@deconstructible
class UnicodeUsernameValidator(validators.RegexValidator):
    regex = r"^[\w.@+-]+\Z"
    message = _(
        "Insira um nome de usuário válido. Este valor pode conter apenas letras, números e os caracteres @/./+/-/_."
    )
    flags = 0



# Password:
def valida_password(value, username=None, old_password=None):
    """
    Realiza uma validação completa de senha
    
    Args:
        value (str): A senha a ser validada
        username (str, optional): Nome de usuário para comparação
        old_password (str, optional): Senha antiga para verificar se não está sendo reutilizada
        
    Raises:
        ValidationError: Se a senha não atender aos critérios de segurança
    """
   
    errors = []
   
    if len(value) < 8:
        errors.append("A senha precisa ter pelo menos 8 caracteres")
    if len(value) > 128:
        errors.append("A senha não pode ter mais que 128 caracteres")
        
   
    if not re.search(r"[A-Z]", value):
        errors.append("A senha precisa ter pelo menos uma letra maiúscula")
    if not re.search(r"[a-z]", value):
        errors.append("A senha precisa ter pelo menos uma letra minúscula")
    if not re.search(r"\d", value):
        errors.append("A senha precisa ter pelo menos um número")
    if not any(char in string.punctuation for char in value):
        errors.append("A senha precisa ter pelo menos um caractere especial")
   
    
        
    sequencias = [
        "12345", "qwert", "asdfg", "zxcvb", "abc", "123", 
        string.ascii_lowercase, string.ascii_uppercase, string.digits
    ]
    for seq in sequencias:
        if any(seq[i:i+3] in value.lower() for i in range(len(seq)-2)):
            errors.append("A senha não pode conter sequências óbvias de caracteres")
            break
        
    if username:
        if username.lower() in value.lower() or value.lower() in username.lower():
            errors.append("A senha não pode conter ou ser similar ao nome de usuário")
    
    if old_password and value == old_password:
        errors.append("A nova senha não pode ser igual à senha anterior")
    
    if value.startswith(' ') or value.endswith(' '):
        errors.append("A senha não pode começar ou terminar com espaços em branco")
        
    if not value.isascii():
        errors.append("A senha deve conter apenas caracteres ASCII")
        
    if errors:
        raise ValidationError(errors)
        
    return value

