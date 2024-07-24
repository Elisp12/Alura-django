from django import forms

class Cadastro_formulario(forms.Form):
    nome_cadastro = forms.CharField(
        label='Nome de Cadastro',
        required=True,
        max_length=100,
        widget=forms.TextInput(
           attrs= {
                'class': 'form-control',
                'placeholder': 'Ex.: João Silva'
           } 
        )
    )

    email = forms.EmailField(
        label='Seu E-mail',
        required=True,
        max_length=150,
        widget=forms.EmailInput(
           attrs= {
                'class': 'form-control',
                'placeholder': 'Ex.: Joãosilva@email.com'
           } 
        )
    )

    senha1 = forms.CharField(
        label='Senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs= {
                'class': 'form-control',
                'placeholder': 'Digite sua senha'
            }
        )
    )

    senha2 = forms.CharField(
        label='Confirme sua Senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs= {
                'class': 'form-control',
                'placeholder': 'Digite sua senha novamente'
            }
        )
    )

    def clean_nome_cadastro(self): # impossibilita espaços no campo
        nome = self.cleaned_data.get('nome_cadastro') 

        if nome:
            nome = nome.strip()
            if " " in nome:
                raise forms.ValidationError('Não é permitido espaços no campo acima! ')
            else:
                return nome