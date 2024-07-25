from django.shortcuts import render, redirect
from django.contrib import messages

from apps.catalogo.models import Peca
from apps.itens.formulario import Item_formulario

def deletar(request, index):
    item = Peca.objects.get(index = index)
    item.delete()

    messages.success(request, 'Item deletado com sucesso!')
    return render(request, 'usuarios/home_usuario.html', context = {})