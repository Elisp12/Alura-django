from django.shortcuts import render

from apps.catalogo.models import Modalidade, Peca

from django.contrib.auth.models import User


def lista_peca(request):
    peca = Peca.objects.all()

    context = {
        'lista_peca': peca
    }
    return render(request, 'peca/lista_peca.html', context = context)