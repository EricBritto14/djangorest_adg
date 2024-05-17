from django.urls import path

from djangoAPI.views import *

urlpatterns = [
    path('produtos/', get_prods, name='produtos'),
    path('produtos/<str:nome>', get_prods_name, name="produtosName"),
    path('data/', user_management)
]