from django.db import models

# Create your models here.
class Produtos(models.Model):
    nome = models.CharField(max_length=200, null=False, unique=True)
    tipo = models.CharField(max_length=200, null=False)
    valor = models.FloatField(max_length=200, null=False)
    quantidade = models.IntegerField(null=False)
    tamanho = models.CharField(max_length=200, null=False)
    data_validade = models.DateField(null=False)
    data_cadastro = models.DateField(null=False)
    
    def __str__(self) -> str:
        return self.nome
    