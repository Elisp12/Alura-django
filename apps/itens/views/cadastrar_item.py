from django.shortcuts import render

def cadastrar_item(request):
    return render(request, 'novo_item/cadastrar_item.html', context = {})