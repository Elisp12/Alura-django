from django.shortcuts import render

context = {
    
}
def buscar_item(request):
    return render(request, 'peca/buscar_item.html', context = context)