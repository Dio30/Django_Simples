from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class UserForm(UserCreationForm):
    username = forms.CharField(required=True, label='Usuário', help_text="Insira seu usuário.", widget=forms.TextInput(attrs={
            'class': 'form-control'
    }))
    email = forms.EmailField(required=True, help_text="Insira um email valido.", widget=forms.TextInput(attrs={
            'class': 'form-control'
    }))
    password1 = forms.CharField(label="Senha", help_text="""<li>Sua senha não pode ser muito parecida com o nome do usuário ou email.</li>
                                    <li>Sua senha precisa conter pelo menos 8 caracteres.</li>
                                    <li>Sua senha não pode ser uma senha comumente utilizada. Ex: aaa, bbb, 1234..., etc.</li>
                                    <li>Sua senha não pode ser inteiramente numérica, use letras juntamente de números ou 
                                    caracteres especiais como @/./+/-/_</li>""", widget=forms.PasswordInput(
                attrs={'placeholder':'Insira sua senha', 'id':'senha1', 'class': 'form-control'}))
    password2 = forms.CharField(label="Confirmar Senha", help_text="Confirme sua senha para verificação.", widget=forms.PasswordInput(
                attrs={'placeholder':'Confirme sua senha', 'id':'senha2', 'class': 'form-control'}))
    
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