from django.shortcuts import render

def lista_peca(request):
    return render(request, 'index.html', context={})