from django.db import models

# Create your models here.
class Colaboradores(models.Model):
    Nomes = models.CharField(max_length=150)
    Equipamento = models.CharField(max_length=150)
    Setor = models.CharField(max_length=100)
    Grupo = models.CharField(max_length=100)