from django.shortcuts import render

def criar_modalidade(request):
    return render(request, 'usuarios/novo_item/criar_modalidade.html', context = {})