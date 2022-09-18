from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import inlineformset_factory



from .models import Mesa, Pedido, pedido_has_prato


class PedidoForm(ModelForm):
	class Meta:
		model = Pedido
		fields = ['numero', 'pratos', 'garcon', 'mesa', 'status']

class PedidoHasPratoForm(ModelForm):
	class Meta:
		model = pedido_has_prato
		fields = '__all__'

class MesaForm(ModelForm):
	class Meta:
		model = Mesa
		fields = '__all__'

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
