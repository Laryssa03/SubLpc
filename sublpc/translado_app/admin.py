from django.contrib import admin
from translado_app.models import * 
admin.site.register(Departamento)
admin.site.register(Funcionario)
admin.site.register(Motorista)
admin.site.register(Veiculo)
admin.site.register(Solicitacao)
admin.site.register(RespSolicitacao)

