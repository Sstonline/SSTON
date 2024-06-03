from django.db import models
from django.contrib.auth.models import User,Permission


# Create your models here.
class emp(models.Model):
    nome = models.CharField(max_length=20)
class unidade(models.Model):
    Nome = models.CharField(max_length=100)
    CNPJ = models.CharField(max_length=100)
    Estado = models.CharField(max_length=100)
    Cidade = models.CharField(max_length=100)
    Endereço = models.CharField(max_length=100)
    Tipo = models.CharField(max_length=100)
    emp = models.ForeignKey(emp, on_delete=models.CASCADE)

class setor(models.Model):
    Nome = models.CharField(max_length=100)
    Unidade = models.ForeignKey(unidade, on_delete=models.CASCADE)
    emp = models.ForeignKey(emp, on_delete=models.CASCADE)

class turno(models.Model):
    Nome = models.CharField(max_length=100)
    Unidade = models.ForeignKey(unidade, on_delete=models.CASCADE)
    Inicio = models.CharField(max_length=100)
    Fim = models.CharField(max_length=100)
    emp = models.ForeignKey(emp, on_delete=models.CASCADE)

class cargo(models.Model):
    Nome = models.CharField(max_length=100)
    Unidade = models.ForeignKey(unidade, on_delete=models.CASCADE)
    acesso_nivel_1 = models.BooleanField(default=False)
    acesso_nivel_2 = models.BooleanField(default=False)
    acesso_nivel_3 = models.BooleanField(default=False)
    emp = models.ForeignKey(emp, on_delete=models.CASCADE)

class relato(models.Model):
    id_user = models.CharField(max_length=100)
    id_res = models.CharField(max_length=100)
    Responsavel = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    Nome = models.CharField(max_length=100)
    Unidade = models.ForeignKey(unidade, on_delete=models.CASCADE)
    Setor = models.ForeignKey(setor, on_delete=models.CASCADE)
    Turno = models.ForeignKey(turno, on_delete=models.CASCADE)
    Cargo = models.ForeignKey(cargo, on_delete=models.CASCADE)
    Atividade = models.CharField(max_length=100)
    Tarefa = models.CharField(max_length=100)
    Pessoa = models.CharField(max_length=100)
    Comportamento = models.CharField(max_length=100)
    Movimento = models.CharField(max_length=100)
    Posição = models.CharField(max_length=100)
    EPI = models.CharField(max_length=100)
    Ambiente = models.CharField(max_length=100)
    Padrão = models.CharField(max_length=100)
    Organização = models.CharField(max_length=100)
    Descrição = models.CharField(max_length=100)
    Correção = models.CharField(max_length=100)
    Data = models.CharField(max_length=100)
    emp = models.ForeignKey(emp, on_delete=models.CASCADE)

class estratificação(models.Model):
    id_user = models.CharField(max_length=100)
    Unidade = models.ForeignKey(unidade, on_delete=models.CASCADE)
    Setor = models.ForeignKey(setor, on_delete=models.CASCADE)
    Turno = models.ForeignKey(turno, on_delete=models.CASCADE)
    Cargo = models.ForeignKey(cargo, on_delete=models.CASCADE)
    Data_ocorrencia = models.CharField(max_length=100)
    Tipo = models.CharField(max_length=100)
    Sexo = models.CharField(max_length=100)
    Idade = models.CharField(max_length=100)
    Hora = models.CharField(max_length=100)
    local = models.CharField(max_length=100)
    Nome = models.CharField(max_length=100)
    Setor_a = models.CharField(max_length=100)
    Data_ad = models.CharField(max_length=100)
    tempo_emp = models.CharField(max_length=100)
    Resumo = models.CharField(max_length=200)
    Lider = models.CharField(max_length=100)
    Supervisor = models.CharField(max_length=100)
    Area_fe = models.CharField(max_length=100)
    Tipo_lesão = models.CharField(max_length=100)
    Causador = models.CharField(max_length=100)
    D_fastamento = models.CharField(max_length=100)
    emp = models.ForeignKey(emp, on_delete=models.CASCADE)