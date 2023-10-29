from django.urls import path
from ecommerce_jogos.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
  path('', ver_lista, name='home'),
  path('update_cart/', update_cart, name='update_cart'),
  path('carrinho/', cart, name='carrinho'),
  path('logout/', LogoutView.as_view(), name='logout')
]