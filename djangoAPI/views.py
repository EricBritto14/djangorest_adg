from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from djangoAPI.models import *
from djangoAPI.serializer import *
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

authentication_classes = [BasicAuthentication]
permission_classes = [IsAuthenticated]

# Create your views here.
@api_view(['GET'])
def get_prods(request):
    #Exibindo todos os produtos do banco
    if request.method == 'GET':
        queryset = Produtos.objects.all()
        authentication_classes = [BasicAuthentication]
        permission_classes = [IsAuthenticated]
        serializer_class = ProdutoSerializer(queryset, many=True)
        return Response(serializer_class.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)
    
    # def post(self, request):
    #     serializer = ProdutoSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)
    
@api_view(['GET'])
def get_prods_name(request, nome):
    try:
        produto = Produtos.objects.get(pk=nome)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST, detail="Produto de nome inexistente!")
    
    if request.method == 'GET':
        serializer = ProdutoSerializer(produto)
        return Response(serializer.data)
    
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def user_management(request):
    #pegando os dados
    if request.method == 'GET':
        try:
            if request.GET['produtos']: #Verifica se tem um parametro chamado "produtos"
                produtos_nome = request.GET['produtos'] #Campo que pega este parametro
                try:
                    produto = Produtos.objects.get(pk=produtos_nome)
                except:
                    return Response(status=status.HTTP_404_NOT_FOUND, detail="Produto não encontrado")
                
                serializer = ProdutoSerializer(produto)
                return Response(serializer.data)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND, detail="Produto de nome inexistente!")
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST, detail="Erro ao fazer o GET")
    
    #criando os dados
    if request.method == 'POST':
        new_prod = request.data
        
        serializer = ProdutoSerializer(data=new_prod)
        
        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST, detail="Produto incoerente")
    
    #Editando os dados
    #1 dos jeitos de editar dados, pelo request.data
    if request.method == 'PUT':
        prod = request.data['nome']
        try:
            update_prod = Produtos.objects.get(pk=prod)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        print(request.data)
        
        serializer = ProdutoSerializer(update_prod, data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
        

class produtosTeste(viewsets.ModelViewSet):
    #Exibindo todos os produtos do banco
    queryset = Produtos.objects.all()
    serializer_class = ProdutoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    