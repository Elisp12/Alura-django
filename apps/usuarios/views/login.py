from django.shortcuts import render, redirect

from apps.usuarios.formulario.login import Login_formulario
from django.contrib import auth
from django.contrib import messages

def login(request):
    form = Login_formulario()

    if request.method == 'POST':
        form = Login_formulario(request.POST)

        if form.is_valid():
            nome = form['nome_login'].value()  
            senha = form['senha'].value()
    
        usuario = auth.authenticate(
            request,
            username = nome,  
            password = senha
        )

        if usuario is not None:
            auth.login(request, usuario)

            messages.success(request, f'{nome} logado com sucesso!')
            return redirect('lista_peca')
        
        else:
            messages.error(request, 'Erro ao efetuar login!')

            return redirect('login')   

    context = {
        'form': form
    }
    return render(request, 'usuarios/login.html', context = context)

'''
    Área para login de usuários

'''