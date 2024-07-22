from django.shortcuts import render

def cadastro(request):

    context = {
        
    }
    return render(request, 'usuarios/cadastro.html', context = context)
