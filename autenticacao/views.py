from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from .forms import UserForm, LoginForm

class UserRegister(SuccessMessageMixin, CreateView):
    form_class = UserForm
    success_message = 'Usuário criado com sucesso!'
    success_url = reverse_lazy('login')
    template_name = 'registro.html'
    
class LoginUser(LoginView):
    template_name='login.html'
    form_class = LoginForm