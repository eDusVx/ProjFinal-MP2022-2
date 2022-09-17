from posixpath import split
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from datetime import datetime, date, timezone
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib import messages
from .forms import CreateUserForm, MesaForm, PedidoForm


def index(request):
    tipos = []
    if 'tipo' in request.GET and request.GET['tipo'] != "":
        tipos = request.GET['tipo'] if type(request.GET['tipo']) in (
            tuple, list) else request.GET['tipo'].split(',')
        pratosRaw = Prato.objects.filter(tipo__in=tipos)
    else:
        tipos = []
        pratosRaw = Prato.objects.all()
    pratos = []
    for prato in pratosRaw:
        ingredientesArray = []
        ingredientes = prato.ingredientes.all()
        has_estoque = True
        for ingrediente in ingredientes:
            quantidade_ingrediente = prato_has_ingrediente.objects.get(
                ingrediente=ingrediente, prato=prato)
            quantidade_ingrediente = quantidade_ingrediente.quantidade
            quantidade = float(ingrediente.quantidade.split('g')[
                               0]) * quantidade_ingrediente

            detalhes = {
                "quantidade": trataDados(quantidade, "g"),
                "valor_energetico": trataDados(ingrediente.valor_energetico * quantidade_ingrediente, ""),
                "carboidratos": trataDados(ingrediente.carboidratos * quantidade_ingrediente, ""),
                "proteinas": trataDados(ingrediente.proteinas * quantidade_ingrediente, ""),
                "gorduras": trataDados(ingrediente.gorduras * quantidade_ingrediente, ""),
                "fibra_alimentar": trataDados(ingrediente.fibra_alimentar * quantidade_ingrediente, ""),
                "sodio": trataDados(ingrediente.sodio * quantidade_ingrediente, ""),
                "acucares": trataDados(ingrediente.acucares * quantidade_ingrediente, ""),
                "colesterol": trataDados(ingrediente.colesterol * quantidade_ingrediente, ""),
            }
            ingredientesArray.append(
                {
                    "ingrediente": ingrediente.nome,
                    "quantidade_total": trataDados(quantidade, "g"),
                    "detalhes": detalhes,
                }
            )
            estoque = Estoque.objects.filter(
                ingrediente=ingrediente, quantidade__gte=quantidade_ingrediente, validade__gte=datetime.now()).values()
            if not list(estoque):
                has_estoque = False

        pratos.append({
            'prato': prato,
            'ingredientes': ingredientesArray,
            'has_estoque': has_estoque,
        })

    context = {
        'pratos': pratos,
        'tipos': tipos,
    }
    return render(request, 'webpage/index.html', context)


def trataDados(dado, tipo):
    if dado % 1 == 0:
        dado = str(
            int(dado))+f" {tipo}" if int(dado) < 1000 else str(int(dado)/1000)+f" k{tipo}"
    else:
        dado = str(f"{dado:,.2f}") + \
            f" {tipo}" if dado < 1000 else str(f"{dado/1000:,.2f}")+f" k{tipo}"
    return dado


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'webpage/funcionario/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')

def home(request):
    current_garcon = Garcon.objects.get(user=request.user)
    orders = Pedido.objects.filter(garcon=current_garcon)
    customers = Mesa.objects.filter(garcon_responsavel=current_garcon)
    total_orders = orders.count()
    delivered = orders.filter(status='Pronto').count()
    pending = orders.filter(status='Fazendo').count() + \
	                        orders.filter(status='Pedido').count()

    context = {'orders': orders, 'customers': customers,
	'total_orders': total_orders, 'delivered': delivered,
    'pending': pending, 'current_garcon': current_garcon}
    return render(request, 'webpage/funcionario/dashboard.html', context)
 
    

    
@login_required(login_url='login')
def numero_mesa(request, pk_test):
    customer = Mesa.objects.get(id=pk_test)

    orders = customer.pedido_set.all()
    order_count = orders.count()
    delivered = orders.filter(status='Pronto').count()
    pending = orders.filter(status='Fazendo').count() + \
        orders.filter(status='Pedido').count()
    context = {'customer': customer, 'orders': orders, 'order_count': order_count, 'delivered': delivered,
               'pending': pending}
    return render(request, 'webpage/funcionario/customer.html', context)


@login_required(login_url='login')
def atualizar_pedido(request, pk):
	current_garcon = Garcon.objects.get(user=request.user)
	current_mesa = Mesa.objects.get(garcon_responsavel =current_garcon)
	order = Pedido.objects.get(id=pk)
	form = PedidoForm(instance=order)

	if request.method == 'POST':
		form = PedidoForm(request.POST, instance=order)
		if form.is_valid():
			form.save()
			return redirect(f'/mesa/{current_mesa}/')


@login_required(login_url='login')
def deletar_pedido(request, pk):
	current_garcon = Garcon.objects.get(user=request.user)
	current_mesa = Mesa.objects.get(garcon_responsavel =current_garcon)
	order = Pedido.objects.get(id=pk)
	if request.method == "POST":
		order.delete()
		return redirect(f'/mesa/{current_mesa}/')

	context = {'item':order}
	return render(request, 'webpage/funcionario/delete.html', context)

@login_required(login_url='login')
def fechar_pedido(request):
	current_garcon = Garcon.objects.get(user=request.user)
	current_mesa = Mesa.objects.get(garcon_responsavel =current_garcon)
	pedido = Pedido.objects.filter(mesa= current_mesa)
	context = {'item':pedido}
	return render(request, 'webpage/funcionario/fechar_pedido.html', context)
