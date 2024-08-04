from django.shortcuts import render, redirect
from django.contrib import messages

from apps.catalogo.models import Modalidade, Peca

def cadastrar_item(request):

    nome = request.POST.get('nome')
    descricao = request.POST.get('descricao')
    relacao = request.POST.get('relacao')
    imagem = request.POST.get('imagem')
    modalidade = request.POST.get('modalidade')

    if request.method == 'POST':
        Peca.objects.update_or_create(nome = nome, descricao = descricao, relacao = relacao, imagem = imagem, modalidade = Modalidade.objects.get(index = modalidade))

        messages.success(request, 'Item criado com sucesso!')
        
        return redirect('home_usuario')
    
    lista_modalidade = Modalidade.objects.all()
    lista_itens = Peca.objects.all()

    context = {
        'lista_item': lista_itens,
        'lista_modalidade': lista_modalidade
    }

    return render(request, 'usuarios/novo_item/cadastrar_item.html', context = context)