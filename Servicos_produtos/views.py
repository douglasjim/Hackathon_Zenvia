from django.shortcuts import render,get_list_or_404,get_object_or_404
from django.http import HttpResponse
from .models import ServicosEProdutos
from urllib import request


def index(request):

    servicos = ServicosEProdutos.objects.all()

    dados = {
        'servicos': servicos
    }

    return render(request,'index.html',dados)

def receita(request, servico_id):
    servico = get_object_or_404(ServicosEProdutos, pk=servico_id)
    servico_a_exibit = {
        'servico': servico
    }
    return render(request,'receita.html',servico_a_exibit)