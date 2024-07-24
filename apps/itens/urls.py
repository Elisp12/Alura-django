from django.urls import path

from .views.cadastrar_item import cadastrar_item
from .views.criar_modalidade import criar_modalidade

urlpatterns = [
    path('cadastrar/item/', cadastrar_item, name= 'cadastrar_item'),
    path('criar/modalidade/', criar_modalidade, name= 'criar_modalidade')
]