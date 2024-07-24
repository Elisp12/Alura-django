from django.shortcuts import render
from apps.catalogo.models import Peca

context = {
    
}
def buscar_item(request):
    item = Peca.objects.all() 
    if "buscar" in request.POST:
        nome_buscar = request.POST['buscar']
        if nome_buscar:
            item = item.filter(nome__icontains= nome_buscar)

    context = {
        'lista_peca' : item
    }
    return render(request, 'peca/buscar_item.html', context = context)

''' 
    Mecanismo de busca 
 - views
 - busca todos os dados inseridos na models
 - conferi se exite request (pesquisa do usuário)
 - compara request com dados na model 
 - fitra as iniciais
 - se verdadeiro, devolve para o usuário
 
'''