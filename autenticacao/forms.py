from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class UserForm(UserCreationForm):
    username = forms.CharField(required=True, label='Usuário', help_text="Insira seu usuário.")
    email = forms.EmailField(required=True, help_text="Insira um email valido.")
    
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        
    def clean_username(self):
        u = self.cleaned_data['username']
        user = User.objects.filter(username=u)
        if user.exists():
            raise forms.ValidationError(f'O usuário {u} já existe.')
        
        if u.isnumeric():
            raise forms.ValidationError('O usuário não pode ser somente numérico.')
        return u
    
    def clean_email(self):
        e = self.cleaned_data['email']
        email = User.objects.filter(email=e).exclude(email='')
        if email.exists():
            raise forms.ValidationError(f'O email {e} já existe.')
        return e

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']