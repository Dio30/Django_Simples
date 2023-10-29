from django.urls import path
from .views import UserRegister, LoginUser

urlpatterns = [
    path('registrar/', UserRegister.as_view(), name='registrar'),
    path('', LoginUser.as_view(), name='login'),
]