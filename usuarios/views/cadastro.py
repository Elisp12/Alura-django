from django.shortcuts import render, redirect

from usuarios.formulario.cadastro import Cadastro_formulario

def cadastro(request):
    form = Cadastro_formulario()

    if form['senha1'].value() != form['senha2'].value(): #condição para senhas de diferentes
        return redirect('cadastro') #retorna a página de cadastro
    
    context = {
        'form': form   
    }
    return render(request, 'usuarios/cadastro.html', context = context)



