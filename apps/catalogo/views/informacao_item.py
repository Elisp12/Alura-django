from django.shortcuts import render

from apps.catalogo.models import Peca

def informacao_item(request, index):
    item = Peca.objects.filter(index = index).all()

    context ={
        'informacao_item': item
    }
    return render(request, 'peca/informacao_item.html', context = context)