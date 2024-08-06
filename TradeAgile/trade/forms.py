# Importações necessárias
from .models import Cliente
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Formulário para o modelo Cliente
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente  # Associa o formulário ao modelo Cliente
        fields = '__all__'  # Inclui todos os campos do modelo no formulário

# Formulário de registro de usuário
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)  # Campo de e-mail obrigatório
    class Meta:
        model = User  # Associa o formulário ao modelo User
        fields = ('username', 'email', 'password1', 'password2')  # Campos incluídos no formulário
