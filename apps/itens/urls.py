from django.urls import path

from .views.cadastrar_item import cadastrar_item
from .views.criar_modalidade import criar_modalidade
from .views.editar import editar
from .views.deletar import deletar

urlpatterns = [
    path('cadastrar/item/', cadastrar_item, name= 'cadastrar_item'),
    path('criar/modalidade/', criar_modalidade, name= 'criar_modalidade'),
    path('editar/', editar, name= 'editar'),
    path('deletar/', deletar, name= 'deletar'),
]