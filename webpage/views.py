from django.http import HttpResponseRedirect
from django.shortcuts import render
from datetime import datetime, date, timezone
from .models import Garcon, Ingrediente, Prato, Estoque
from .forms import Login

def index(request):
    pratosRaw = Prato.objects.all()
    pratos = []
    for prato in pratosRaw:
        ingredientes = prato.ingredientes.all()
        for ingrediente in ingredientes:
            has_estoque = Estoque.objects.filter(ingrediente=ingrediente,quantidade__gt=0,validade__gte=datetime.now()).values()
            if not list(has_estoque):
                has_estoque = False
                break
                
        pratos.append({
            'prato': prato,
            'ingredientes': prato.ingredientes.all(),
            'has_estoque': has_estoque
        })
        
    context = {
        'pratos': pratos
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
