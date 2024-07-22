from django.shortcuts import render

from usuarios.forms import Login_formulario

def login(request):
    form = Login_formulario()

    context = {
        'form': form
    }
    return render(request, 'usuarios/login.html', context = context)

'''
    Área para login usuários

'''