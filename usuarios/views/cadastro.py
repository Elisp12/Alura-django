from django.shortcuts import render, redirect

from usuarios.formulario.cadastro import Cadastro_formulario
from django.contrib.auth.models import User
from django.contrib import messages

def cadastro(request):
    form = Cadastro_formulario()

    if request.method == 'POST': # se o usuário fizer input
        form = Cadastro_formulario(request.POST) # pega dados do input e passa para formulário

        if form.is_valid():

            nome = form['nome_cadastro'].value() # valores passados por usuários
            email = form['email'].value()
            senha = form['senha1'].value()

            if User.objects.filter(username = nome).exists(): # se usuário já exite
                
                messages.error(request, 'Usuário jé existente')
                
                return redirect('cadastro')
            
            usuario = User.objects.create_user( # cria novo usuário no banco de dados
                username = nome,
                email = email,
                password = senha
            )
            usuario.save() 

            messages.success(request, 'Cadastro efetuado com sucesso!')

            return redirect('login') # redireciona para página de login
    
    context = {
        'form': form   
    }
    return render(request, 'usuarios/cadastro.html', context = context)



