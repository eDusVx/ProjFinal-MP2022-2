from posixpath import split
from django.http import HttpResponseRedirect
from django.shortcuts import render
from datetime import datetime, date, timezone
from .models import Garcon, Ingrediente, Prato, Estoque, prato_has_ingrediente
from .forms import Login

def index(request):
    tipos = []
    if 'tipo' in request.GET and request.GET['tipo'] != "":
        tipos = request.GET['tipo'] if type(request.GET['tipo']) in (tuple, list) else request.GET['tipo'].split(',')
        pratosRaw = Prato.objects.filter(tipo__in=tipos)
    else:
        tipos = []
        pratosRaw = Prato.objects.all()
    pratos = []
    for prato in pratosRaw:
        ingredientesArray= []
        ingredientes = prato.ingredientes.all()
        has_estoque = True
        for ingrediente in ingredientes:
            quantidade_ingrediente = prato_has_ingrediente.objects.get(ingrediente=ingrediente, prato=prato)
            quantidade_ingrediente = quantidade_ingrediente.quantidade
            quantidade = float(ingrediente.quantidade.split('g')[0]) * quantidade_ingrediente
        
            detalhes = {
                "quantidade": trataDados(quantidade,"g"),
                "valor_energetico": trataDados(ingrediente.valor_energetico * quantidade_ingrediente,""),
                "carboidratos": trataDados(ingrediente.carboidratos * quantidade_ingrediente,""),
                "proteinas": trataDados(ingrediente.proteinas * quantidade_ingrediente,""),
                "gorduras": trataDados(ingrediente.gorduras * quantidade_ingrediente,""),
                "fibra_alimentar": trataDados(ingrediente.fibra_alimentar * quantidade_ingrediente,""),
                "sodio": trataDados(ingrediente.sodio * quantidade_ingrediente,""),
                "acucares": trataDados(ingrediente.acucares * quantidade_ingrediente,""),
                "colesterol": trataDados(ingrediente.colesterol * quantidade_ingrediente,""),
            }
            ingredientesArray.append(
                {
                    "ingrediente": ingrediente.nome,
                    "quantidade_total": trataDados(quantidade,"g"),
                    "detalhes": detalhes,
                }
            )
            estoque = Estoque.objects.filter(ingrediente=ingrediente,quantidade__gte=quantidade_ingrediente,validade__gte=datetime.now()).values()
            if not list(estoque):
                has_estoque = False     
                
        pratos.append({
            'prato': prato,
            'ingredientes': ingredientesArray,
            'has_estoque': has_estoque,
        })
        
    context = {
        'pratos': pratos,
        'tipos': tipos
    }
    return render(request, 'webpage/index.html', context)

def login(request):
    if request.method == 'POST':
        form = Login(request.POST)
        req = request.POST
        if form.is_valid():
            garçon = Garcon.objects.filter(email=req['email']).values()
            print(garçon)
            form = Login()
            return HttpResponseRedirect('/thanks/')
    return render(request,'webpage/funcionario/login.html', {'form': Login})


def trataDados(dado,tipo):
    if dado % 1 == 0:
        dado = str(int(dado))+f" {tipo}" if int(dado) < 1000 else str(int(dado)/1000)+f" k{tipo}"
    else:
        dado = str(dado)+f" {tipo}" if dado < 1000 else str(dado/1000)+f" k{tipo}"
    return dado