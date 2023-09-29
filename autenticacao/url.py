from django.urls import path
from .views import UserRegister, LoginUser
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('registrar/', UserRegister.as_view(), name='registrar'),
    path('', LoginUser.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout')
]