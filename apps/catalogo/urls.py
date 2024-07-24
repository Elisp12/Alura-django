from django.urls import path

from apps.catalogo.views.lista_peca import lista_peca
from apps.catalogo.views.informacao_item import informacao_item
from apps.catalogo.views.buscar_item import buscar_item

urlpatterns = [
    path('', lista_peca, name='lista_peca'),
    path('informacao/<int:index>/', informacao_item, name='informacao_item'),
    path('buscar/item/', buscar_item, name='buscar_item')
]
