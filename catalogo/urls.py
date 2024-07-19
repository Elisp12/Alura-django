from django.urls import path

from .views.lista_peca import lista_peca

urlpatterns = [
    path('', lista_peca, name='lista_peca')
]
