from django.contrib import admin
from .models import ServicosEProdutos

# a parte la do django onde adicionamos os servicos etcc. fica nesta linha se a gente a apagar essa opcao vai sumir
admin.site.register(ServicosEProdutos)

