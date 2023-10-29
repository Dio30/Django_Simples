from django import forms
from .models import Jogos

class JogosForm(forms.ModelForm):
    class Meta:
        model = Jogos
        fields = ['nome_jogo', 'preco', 'detalhes', 'imagem']