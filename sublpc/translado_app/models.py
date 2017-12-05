from django.contrib.auth.models import User
from django.db import models

class Departamento(models.Model):
    nome = models.CharField(max_length=128)
    cod = models.IntegerField(max_length=10)

    def __str__(self):
        return self.nome 

class Funcionario(models.Model):
    nome = models.CharField(max_length=128)
    cpf=models.CharField(max_length=128)
    usuario = models.ForeignKey(User, null=True, blank=False)
    departamento = models.ForeignKey(Departamento, null=True, blank=False)
    TIPO_CHOICES = (
        ('Chefe', 'Chefe'),
        ('Administrativo', 'Administrativo'),
    )
    tipo = models.CharField(max_length=25, choices=TIPO_CHOICES, blank=False, null=False)
    def __str__(self):
        return self.nome + " ( " + self.tipo + " )"

class Solicitacao(models.Model):
    solicitante = models.ForeignKey(Funcionario, null=True, blank=False)
    dataH_inicio = models.DateTimeField(blank=True, null=True)
    dataH_fim = models.DateTimeField(blank=True, null=True)
    origem = models.CharField(max_length=128)
    destino = models.CharField(max_length=128)
    motivo = models.CharField(max_length=128)
    
    def __str__(self):
        return self.motivo 
    
class Veiculo(models.Model):
    placa = models.CharField(max_length=8)
    modelo = models.CharField(max_length=35)
    ano = models.IntegerField(max_length=4)

    def __str__(self):
        return self.placa
class Motorista(models.Model):
    nome = models.CharField(max_length=128)
    cnh=models.CharField(max_length=128)
 
    def __str__(self):
        return self.nome
class RespSolicitacao(models.Model):
    veiculo = models.ForeignKey(Veiculo, null=True, blank=False)
    motorista= models.ForeignKey(Motorista, null=True, blank=False)
    solicitacao = models.OneToOneField(Solicitacao, null=True, blank=False)
 
    def __str__(self):
        return self.veiculo + " ( " + self.motorista + " )"