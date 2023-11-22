from django.db import models


class Empresa(models.Model):
    nome = models.CharField(max_length=50)


class ExperienciaProfissional(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    cargo = models.CharField(max_length=50, blank=True, null=True)
    instituicao_academica = models.CharField(max_length=100)
    curso = models.CharField(max_length=100)


class Pessoa(models.Model):
    nome = models.CharField(max_length=50, null=True, blank=True)
    endereco = models.CharField(max_length=50, null=True, blank=True)
    telefone = models.CharField(max_length=9, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    resumo = models.TextField(null=True, blank=True)
    experiencia_profissional = models.ForeignKey(ExperienciaProfissional, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nome
