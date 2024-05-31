# forms.py
from django import forms

class CadastroForm(forms.Form):
    nome = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Nome'}))
    cpf = forms.CharField(max_length=11, widget=forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'CPF'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'input-field', 'placeholder': 'Email'}))
    senha = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input-field', 'placeholder': 'Senha'}))
    data_nascimento = forms.DateField(widget=forms.DateInput(attrs={'class': 'input-field', 'type': 'date', 'placeholder': 'Data de Nascimento'}))
    telefone = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Telefone'}))

class Login(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'input-field', 'placeholder': 'Email'}))
    senha = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input-field', 'placeholder': 'Senha'}))