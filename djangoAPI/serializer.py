from rest_framework import serializers
from djangoAPI.models import *

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produtos
        fields = ['nome', 'tipo', 'valor', 'quantidade', 'tamanho', 'data_validade', 'data_cadastro']