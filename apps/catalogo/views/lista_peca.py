from django.shortcuts import render, redirect

from apps.catalogo.models import Modadalidade, Peca
from django.contrib import messages
from django.contrib.auth.models import User


def lista_peca(request):
    peca = Peca.objects.all()
    
    

    context = {
        'lista_peca': peca
    }
    return render(request, 'peca/lista_peca.html', context = context)