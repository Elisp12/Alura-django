from django.urls import path

from .views.lista_peca import lista_peca
from .views.informacao_item import informacao_item

urlpatterns = [
    path('', lista_peca, name='lista_peca'),
    path('informacao/<int:index>/', informacao_item, name='informacao_item'),
]
