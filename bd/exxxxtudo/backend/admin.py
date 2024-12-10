from django.contrib import admin
from .models import Cliente, Endereco, Perfil, Servico, TipoServico

admin.site.register(Cliente)
admin.site.register(Endereco)
admin.site.register(Perfil)
admin.site.register(Servico)
admin.site.register(TipoServico)
