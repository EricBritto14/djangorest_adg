from django.shortcuts import render
from rest_framework import viewsets
from djangoAPI.models import *
from djangoAPI.serializer import *

# Create your views here.
class produtosView(viewsets.ModelViewSet):
    #Exibindo todos os produtos do banco
    queryset = Produtos.objects.all()
    serializer_class = ProdutoSerializer
    
