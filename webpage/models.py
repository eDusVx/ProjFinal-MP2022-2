from tkinter import CASCADE
from django.db import models
from django import forms

# Create your models here.
    
class Garcon(models.Model):
    nome_completo = models.CharField(max_length=350)
    email = models.CharField(unique=True,max_length=150)
    password = models.CharField(max_length=150)
    def __str__(self):
        return self.nome_completo
    
class Pedido(models.Model):
    numero = models.IntegerField(max_length=1000)
    pratos = models.TextField()

class Mesa(models.Model):
    numero = models.IntegerField(max_length=3)
    pedidos = models.ManyToManyField(Pedido)
    garcon_responsavel = models.ForeignKey(Garcon, on_delete=models.CASCADE)
    
