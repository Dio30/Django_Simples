from django.db import models
from django.conf import settings

class Jogos(models.Model):
    nome_jogo = models.CharField(max_length=200, null=True, blank=True, verbose_name='Nome do Jogo')
    preco = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Preço (R$)')
    detalhes = models.CharField(max_length=200, null=True, blank=True)
    imagem = models.ImageField(null=True, blank=True, upload_to='jogos')
    
    def __str__(self):
        return self.nome_jogo
    
    class Meta:
        verbose_name = 'Jogo'
        verbose_name_plural = 'Jogos'
    
    @property 
    def image_url(self): # para poder visualizar fotos no html
        if self.imagem and hasattr(self.imagem, 'url'):
            return self.imagem.url

class Pedidos(models.Model):
    cliente = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    data_pedido = models.DateTimeField(auto_now=True, verbose_name='Data do pedido')
    complete = models.BooleanField(default=False, null=False, blank=False, verbose_name='Pedido foi Completado')
    
    def __str__(self):
        return f'Cliente {self.cliente}'
    
    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
    
    @property
    def pegar_carrinho_total(self):
        itens = self.itenspedido_set.all()
        total = sum([item.pegar_total for item in itens])
        return total
    
    @property
    def pegar_carrinho_itens(self):
        itens = self.itenspedido_set.all()
        total = sum([item.quantidade for item in itens])
        return total

class ItensPedido(models.Model):
    cliente = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    jogo = models.ForeignKey(Jogos, on_delete=models.SET_NULL, null=True, blank=True)
    pedido = models.ForeignKey(Pedidos, on_delete=models.SET_NULL, null=True, blank=True)
    quantidade = models.IntegerField(default=0, null=True, blank=True)
    data_adicao = models.DateTimeField(auto_now=True, null=True, blank=True)
    
    class Meta:
        verbose_name = 'Item_Pedido'
        verbose_name_plural = 'Itens_Pedidos'
    
    def __str__(self):
        return str(f'Item {self.jogo} feito pelo cliente {self.cliente}')
    
    @property
    def pegar_total(self):
        total = self.jogo.preco * self.quantidade
        return total