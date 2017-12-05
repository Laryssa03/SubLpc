from rest_framework import routers, serializers, viewsets
from translado_app.models import *

class DepartamentoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Departamento
        fields = '__all__'
class FuncionarioSerializer(serializers.HyperlinkedModelSerializer):
  
    class Meta:
        model = Funcionario
        fields = '__all__'
class VeiculoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Veiculo
        fields = '__all__'
class MotoristaSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Motorista
        fields = '__all__'
class SolicitacaoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Solicitacao
        fields = '__all__'
class RespSolicitacaoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = RespSolicitacao
        fields = '__all__'