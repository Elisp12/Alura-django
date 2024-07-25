from django.shortcuts import render

from apps.catalogo.models import Peca
from apps.itens.formulario import Item_formulario

def peca_da_modalidade(request, index):
    item = Peca.objects.filter(modalidade = index).all()
    
    context = {
        'peca_da_modalidade': item
    }
    return render(request, 'peca/peca_da_modalidade.html', context = context)