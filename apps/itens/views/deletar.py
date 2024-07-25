from django.shortcuts import render

def deletar(request):
    return render(request, 'peca/informacao_item.html', context = {})