from django.shortcuts import render

from usuarios.formulario.cadastro import Cadastro_formulario

def cadastro(request):
    form = Cadastro_formulario()

    context = {
        'form': form   
    }
    return render(request, 'usuarios/cadastro.html', context = context)
