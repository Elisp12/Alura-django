from django.urls import path

from .views.cadastrar_item import cadastrar_item
from .views.editar import editar
from .views.deletar import deletar
from .views.peca_modalidade import  peca_da_modalidade

urlpatterns = [
    path('cadastrar/item/', cadastrar_item, name= 'cadastrar_item'),
    path('editar/item/<int:index>', editar, name= 'editar_item'),
    path('deletar/item/<int:index>', deletar, name= 'deletar_item'),
    path('peca/da/modalidade/<int:index>/', peca_da_modalidade, name= 'peca_da_modalidade')
]