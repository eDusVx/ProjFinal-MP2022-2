from tkinter import CASCADE
from django.db import models
from django import forms

# Create your models here.
    
class Garcon(models.Model):
    nome_completo = models.CharField(max_length=350)
    email = models.CharField(unique=True,max_length=150,default="default@email.com")
    password = models.CharField(max_length=150,default="admin123456")
    def __str__(self):
        return self.nome_completo

class Mesa(models.Model):
    numero = models.IntegerField(max_length=3)
    garcon_responsavel = models.ForeignKey(Garcon, on_delete=models.CASCADE)
    
class Pedido(models.Model):
    numero = models.IntegerField(max_length=1000)
    pratos = models.TextField()
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE)

class Prato(models.Model):
    nome = models.CharField(max_length=350)
    foto = models.ImageField(upload_to ='Images')
    preco = models.FloatField(max_length=100,default=100.00)


    
