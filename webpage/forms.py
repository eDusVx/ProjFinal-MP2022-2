from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import inlineformset_factory



from .models import Mesa, Pedido, pedido_has_prato

class PedidoForm(ModelForm):
	"""Classe referente ao formulario da tabela do modelo do pedido
	
	:RECEBE:
	:ModelForm: Modelo padrao
	"""
	class Meta:
		model = Pedido
		fields = ['numero', 'pratos', 'garcon', 'mesa', 'status']

class PedidoHasPratoForm(ModelForm):
	"""Classe referente ao formulario da tabela de relacao de pertencimento entre o pedido e o prato
	
	:RECEBE:
	:ModelForm: Modelo padrao"""
	class Meta:
		model = pedido_has_prato
		fields = '__all__'

class MesaForm(ModelForm):
	"""Classe referente ao formulario da tabela do modelo da mesa
	:RECEBE:
	:ModelForm: Modelo padrao"""
	class Meta:
		model = Mesa
		fields = '__all__'

class CreateUserForm(UserCreationForm):
	"""Classe referente a criacao de usuario no sistema
	
	:ATRIBUTOS:
	:UserCreationForm: Formulario de criacao de usuario"""
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
