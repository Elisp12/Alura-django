from django.shortcuts import render, redirect

from django.contrib import messages


from apps.catalogo.models import Peca


def home_usuario(request):

    if not request.user.is_authenticated: # se usuario não estiver logado
        messages.error(request, "Usuário não logado!")
        return redirect('login') # redireciona para página de login
    
    else: # se logado
        lista_peca = Peca.objects.all() #lista todos os itens cadastrados

    context = {
        'lista_peca': lista_peca
    }

    return render(request, 'usuarios/home_usuario.html', context= context)