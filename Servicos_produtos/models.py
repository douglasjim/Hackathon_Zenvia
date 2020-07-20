from django.db import models
from datetime import datetime

class ServicosEProdutos(models.Model):
    nome_servicos_produtos = models.CharField(max_length=200)
    descricao = models.TextField()
    faixa_de_preco = models.CharField(max_length=200)
    validade_do_anuncio = models.CharField(max_length=200)
    aceita_negociacoes = models.BooleanField(default=False)
    telefone = models.IntegerField(max_length=14) # ERRO VERFICICAR
    endereco = models.CharField(max_length=300)
    cidade = models.CharField(max_length=200)
    cpf_ou_cnpj = models.IntegerField(max_length=15) # ERRO VERFICICAR
    data = models.DateField(default=datetime.now,blank=True)

