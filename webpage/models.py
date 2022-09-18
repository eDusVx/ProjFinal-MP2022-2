from secrets import choice
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from django.db import models
from django.contrib import admin
from django import forms
from datetime import datetime, timezone
from djmoney.models.fields import MoneyField
from django.forms import ModelForm
from django.contrib.auth.models import User

# Create your models here.

CHOICES = [("Pedido","Pedido"), ("Fazendo","Fazendo"), ("Pronto","Pronto")]
TIPO_PRATO = [("Entrada","Entrada"),("Executivo","Executivo"),("Carne","Carne"),("Peixe","Peixe"),("Frango","Frango"),("Massa","Massa"),("Vegano/Vegetariano","Vegano/Vegetariano"),("Bebidas","Bebidas"),("Sobremesa","Sobremesa")]
class Garcon(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,default = 1)
    nome_completo = models.CharField(max_length=350)
    email = models.CharField(unique=True,max_length=150,default="default@email.com")
    password = models.CharField(max_length=150,default="admin123456")
    def __str__(self):
        return self.nome_completo.upper()

class Mesa(models.Model):
    numero = models.IntegerField(max_length=3)
    quantidade = models.IntegerField(max_length=2, blank=True, null=True, default=0)
    garcon_responsavel = models.ForeignKey(Garcon, on_delete=models.CASCADE, blank=True, null=True, default=None)
    def __str__(self):
        return str(self.numero)

class Ingrediente(models.Model):
    nome = models.CharField(max_length=350)
    quantidade = models.CharField(max_length=1000,default="100g")
    valor_energetico = models.FloatField(max_length=100,default=0)
    carboidratos = models.FloatField(max_length=100,default=0)
    proteinas = models.FloatField(max_length=100,default=0)
    gorduras = models.FloatField(max_length=100,default=0)
    fibra_alimentar = models.FloatField(max_length=100,default=0)
    sodio = models.FloatField(max_length=100,default=0)
    acucares = models.FloatField(max_length=100,default=0)
    colesterol = models.FloatField(max_length=100,default=0)
    def __str__(self):
        return self.nome.upper()
    
class Prato(models.Model):
    nome = models.CharField(max_length=350)
    foto = models.ImageField(upload_to ='Images')
    preco = MoneyField(max_digits=14, decimal_places=2, default_currency='BRL')
    tipo = models.CharField(max_length=100, choices=TIPO_PRATO, default=None)
    ingredientes = models.ManyToManyField(Ingrediente, through='prato_has_ingrediente')
    def __str__(self):
        return self.nome.upper()
    
class Pedido(models.Model):
    numero = models.IntegerField(max_length=1000)
    pratos = models.TextField()
    garcon = models.ForeignKey(Garcon, on_delete=models.CASCADE, default=0)
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE)
    prato = models.ManyToManyField(Prato, through='pedido_has_prato')    
    status = models.CharField(max_length=100, choices=CHOICES, default="Pedido")

class pedido_has_prato(models.Model):
    prato = models.ForeignKey(Prato, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    quantidade = models.IntegerField(max_length=3, default=0)

class prato_has_ingrediente(models.Model):
    prato = models.ForeignKey(Prato, on_delete=models.CASCADE)
    ingrediente = models.ForeignKey(Ingrediente, on_delete=models.CASCADE)
    quantidade = models.FloatField(max_length=3)

class Estoque(models.Model):
    ingrediente = models.ForeignKey(Ingrediente, on_delete=models.CASCADE)
    quantidade = models.IntegerField(max_length=3)
    validade = models.DateField(default=datetime.now())
    
class pedido_has_prato_inline(admin.TabularInline):
    model = pedido_has_prato
    extra = 1
    
class pedidoAdmin(admin.ModelAdmin):
    inlines = (pedido_has_prato_inline,)
    
class pratoPAdmin(admin.ModelAdmin):
    inlines = (pedido_has_prato_inline,)
    
class prato_has_ingrediente_inline(admin.TabularInline):
    model = prato_has_ingrediente
    extra = 1
    
class ingredienteAdmin(admin.ModelAdmin):
    inlines = (prato_has_ingrediente_inline,)
    
class pratoIAdmin(admin.ModelAdmin):
    inlines = (prato_has_ingrediente_inline,)
