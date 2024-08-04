from django.db import models

from django.contrib.auth.models import User

class Modalidade(models.Model):
    index = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=30, null=False)

    def __str__(self):
        return self.nome
    

class Peca(models.Model):
    index = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=30, null=False)
    descricao = models.TextField()
    relacao = models.CharField( choices= (('velocidade','velocidade'), ('unica','unica')), max_length=250, null=False)
    imagem = models.ImageField(upload_to= 'media/imagem/%Y/%m/%d/', blank=True)
    modalidade = models.ForeignKey(Modalidade, on_delete = models.CASCADE)
    usuario = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name='user'
    )

    def __str__(self):
        return self.nome