from django.shortcuts import render

from apps.itens.formulario import Item_formulario

def cadastrar_item(request):
    form_item = Item_formulario()

    context = {
        'form' : form_item
    }

    return render(request, 'usuarios/novo_item/cadastrar_item.html', context = context)