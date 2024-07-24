from django.shortcuts import render, redirect

from django.contrib import messages

from apps.itens.formulario import Item_formulario

def cadastrar_item(request):
    form = Item_formulario

    if request.method == 'POST':
        form = Item_formulario(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Novo item Cadastrado!')
            return redirect('home_usuario')
        else:
            messages.error(request, 'error')
        
        print(form)
        
    context = {
        'form' : form
    }

    return render(request, 'usuarios/novo_item/cadastrar_item.html', context = context)