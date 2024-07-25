from django.shortcuts import render, redirect
from django.contrib import messages

from apps.catalogo.models import Peca
from apps.itens.formulario import Item_formulario

def editar(request, index):
    item = Peca.objects.get(index=index)
    form = Item_formulario(instance=item)
    
    if request.method == 'POST':
        form = Item_formulario(request.POST, request.FILES, instance= item)

        if form.is_valid():
            form.save()
            messages.success(request, 'Item editado com sucesso!')
            return redirect('home_usuario')
        else:
            messages.error(request, 'error')

    context = {
        'form': form,
        'index': index
    }
    return render(request, 'peca/editar_item.html', context = context)