from django.shortcuts import redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib import messages

def logout(request):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado!")
        return redirect('login')
    else:
        auth.logout(request)
        messages.success(request, 'Logout efetuado com sucesso!')

    return redirect('lista_peca')