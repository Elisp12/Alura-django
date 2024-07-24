from django import forms

from apps.catalogo.models import Peca


class Item_formulario(forms.ModelForm):
    class Meta:
        model = Peca
        fields = "__all__"


        widgets = {
            'nome' : forms.TextInput(attrs= {'class' : 'form-control'}),
            'descricao' : forms.Textarea(attrs= {'class' : 'form-control'}),
            'relacao' : forms.Select(attrs= {'class' : 'form-control'}),
            'imagem' : forms.FileInput(attrs= {'class' : 'form-control'}),
            'usuario' : forms.Select(attrs= {'class' : 'form-control'}), 
        }