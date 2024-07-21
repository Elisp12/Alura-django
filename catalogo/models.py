from django.db import models

class Modadalidade(models.Model):
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
    modalidade = models.ForeignKey(Modadalidade, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.nome