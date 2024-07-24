from django.shortcuts import render
from apps.catalogo.models import Peca

def user_informacao_item(request, index):
    infor = Peca.objects.filter(index=index).all()

    context ={
        'informacao_item': infor
    }
    return render(request, 'peca/informacao_item.html', context = context)