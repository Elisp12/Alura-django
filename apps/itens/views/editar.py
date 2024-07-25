from django.shortcuts import render

def editar(request):
    return render(request, 'peca/informacao_item.html', context ={})