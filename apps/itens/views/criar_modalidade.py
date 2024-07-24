from django.shortcuts import render

def criar_modalidade(request):
    return render(request, 'novo_item/criar_modalidade.html', context = {})