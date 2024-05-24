from django.db import models
from clientes.models import Cliente
from secrets import token_hex
from .choices import ChoicesCategoriasManutencao
from datetime import datetime

class CategoriaManutencao(models.Model):
    titulo = models.CharField(max_length=3, choices=ChoicesCategoriasManutencao.choices)
    preco = models.DecimalField(max_digits=9, decimal_places=2)
    
    def __str__(self) -> str:
        return self.titulo

class Servico(models.Model):
    titulo = models.CharField(max_length=30)
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)
    categoria_manutencao = models.ManyToManyField(CategoriaManutencao)
    data_inicio = models.DateField(null=True)
    data_entrega = models.DateField(null=True)
    finalizado = models.BooleanField(default=True)
    protocolo = models.CharField(max_length=52, null=True, blank=True)
    
    def __str__(self) -> str:
        return self.titulo
    
    def save(self, *args,  **kwargs):
        if not self.protocolo:
            self.protocolo = datetime.now().strftime("%d/%m/%y-%H:%M:%S-") + token_hex(12)
        super(Servico, self).save(*args, **kwargs)

    def preco_total(self):
        preco_total = float(0)
        for categoria in self.categoria_manutencao.all():
           preco_total += float(categoria.preco)
           
        return preco_total 