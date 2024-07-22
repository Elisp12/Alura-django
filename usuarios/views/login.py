from django.shortcuts import render

def login(request):

    context = {

    }
    return render(request, 'usuarios/login.html', context = context)

'''
    Área para login usuários

'''