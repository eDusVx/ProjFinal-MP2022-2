from django.shortcuts import render
from datetime import datetime, timezone
from .models import Garcon, Ingrediente, Prato, Estoque

def index(request):
    pratosRaw = Prato.objects.all()
    pratos = []
    for prato in pratosRaw:
        ingredientes = prato.ingredientes.all()
        for ingrediente in ingredientes:
            has_estoque = Estoque.objects.filter(ingrediente=ingrediente,quantidade__gt=0,validade__gte=datetime.now()).values()
            if not list(has_estoque):
                has_estoque = False
                
        pratos.append({
            'prato': prato,
            'ingredientes': prato.ingredientes.all(),
            'has_estoque': has_estoque
        })
        
    context = {
        'garcons': Garcon.objects.all(),
        'pratos': pratos
    }
    return render(request, 'webpage/index.html', context)
