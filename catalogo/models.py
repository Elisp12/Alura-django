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
    relacao = models.CharField( choices= (('vl','velocidades'), ('un','unica')), max_length=250, null=False)
    modalidade = models.ForeignKey(Modadalidade, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.nome