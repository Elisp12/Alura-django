from django.shortcuts import render

from apps.catalogo.models import Modadalidade, Peca

def lista_peca(request):
    peca = Peca.objects.all()

    context = {
        'lista_peca': peca
    }
    return render(request, 'peca/lista_peca.html', context = context)