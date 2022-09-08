from posixpath import split
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from datetime import datetime, date, timezone
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *
from django.forms import inlineformset_factory
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import OrderForm, CreateUserForm, MesaForm
from .filters import OrderFilter

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


def trataDados(dado,tipo):
    if dado % 1 == 0:
        dado = str(int(dado))+f" {tipo}" if int(dado) < 1000 else str(int(dado)/1000)+f" k{tipo}"
    else:
        dado = str(dado)+f" {tipo}" if dado < 1000 else str(dado/1000)+f" k{tipo}"
    return dado


def registerPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('login')
			

		context = {'form':form}
		return render(request, 'webpage/funcionario/register.html', context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

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
	orders = Pedido.objects.all()
	customers = Mesa.objects.all()

	total_customers = customers.count()

	total_orders = orders.count()
	delivered = orders.filter(status='Pronto').count()
	pending = orders.filter(status='Fazendo').count() + orders.filter(status='Pedido').count()

	context = {'orders':orders, 'customers':customers,
	'total_orders':total_orders,'delivered':delivered,
	'pending':pending }

	return render(request, 'webpage/funcionario/dashboard.html', context)

@login_required(login_url='login')
def numero_mesa(request, pk_test):
	customer = Mesa.objects.get(id=pk_test)

	orders = customer.pedido_set.all()
	order_count = orders.count()
	delivered = orders.filter(status='Pronto').count()
	pending = orders.filter(status='Fazendo').count() + orders.filter(status='Pedido').count()
	context = {'customer':customer, 'orders':orders, 'order_count':order_count,'delivered':delivered,
	'pending':pending}
	return render(request, 'webpage/funcionario/customer.html',context)

@login_required(login_url='login')

def registrar_mesa(request):
	form = MesaForm()
	if request.method == 'POST':
		form = MesaForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/funcionarios/')

	context = {'form':form}
	return render(request, 'webpage/funcionario/mesa_form.html', context)

@login_required(login_url='login')
def atualizar_pedido(request, pk):

	order = Pedido.objects.get(id=pk)
	form = OrderForm(instance=order)

	if request.method == 'POST':
		form = OrderForm(request.POST, instance=order)
		if form.is_valid():
			form.save()
			return redirect('/funcionarios/')

	context = {'form':form}
	return render(request, 'webpage/funcionario/order_form.html', context)

@login_required(login_url='login')
def deletar_pedido(request, pk):
	order = Pedido.objects.get(id=pk)
	if request.method == "POST":
		order.delete()
		return redirect('/funcionarios/')

	context = {'item':order}
	return render(request, 'webpage/funcionario/delete.html', context)
