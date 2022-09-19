from unittest import TestCase
import pytest
from django import urls
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from webpage.models import Garcon, Mesa, Pedido

@pytest.mark.django_db
@pytest.mark.parametrize('param', [
	('index'),
    ('login'),

])
def test_views_sem_login(client, param):
    """Teste para testar a tela inicial sem login
	
	:RECEBE:
	:client: Simulacao do cliente na url testada
	"""
    temp_url = urls.reverse(param)
    resp = client.get(temp_url)
    assert resp.status_code == 200

@pytest.mark.django_db
def test_loginPage(client, create_test_user, user_data):
	"""Teste da pagina de login

	:RECEBE:
	:client: Simulacao do cliente na url testada
	:user_data: Dados de usuario cadastrado
	"""
	login_url = urls.reverse('login')
	resp = client.post(login_url, data=user_data)
	assert resp.status_code == 302
	assert resp.url == urls.reverse('home')


@pytest.mark.django_db
def test_logoutUser(client, authenticated_user):
	"""Teste para logout de usuario

	:RECEBE:
	:client: Simulacao do cliente na url testada
	:authenticated_user: Usuario autenticado no sistema
	"""
	logout_url = urls.reverse('logout')
	resp = client.get(logout_url)
	assert resp.status_code == 302
	assert resp.url == urls.reverse('login')

@pytest.mark.django_db
def test_Home(client,user_data):
	"""Teste da pagina Home
	
	:RECEBE:
	:client: Simulacao do cliente na url testada
	:user_data: Dados de usuario cadastrado
	"""
	login_url = urls.reverse('home')
	resp = client.post(login_url, data=user_data)
	assert resp.status_code == 302

@pytest.mark.django_db
def test_nuemro_mesa(client):
    """Teste para verificar o numero da mesa
	
	:RECEBE:
	:client: Simulacao do cliente na url testada"""
    mesa = Mesa.objects.create(numero=1, quantidade = 3)
    logout_url = urls.reverse('customer', args=[mesa.pk])
    resp = client.get(logout_url)
    assert resp.status_code == 302

@pytest.mark.django_db
def test_atualizar_pedido(client):
    """Teste para atualizar pedido
	
	:RECEBE:
	:client: Simulacao do cliente na url testada"""
    pedido = Pedido.objects.create(numero =1,mesa_id = 1,garcon_id = 1)
    temp_url = urls.reverse('update_order', args=[pedido.pk])
    resp = client.get(temp_url)
    assert resp.status_code == 302

@pytest.mark.django_db
def test_deletar_pedido(client):
	"""Teste para deletar pedido
	
	:RECEBE:
	:client: Simulacao do cliente na url testada"""
	pedido = Pedido.objects.create(numero =1,mesa_id = 1,garcon_id = 1)
	temp_url = urls.reverse('delete_order', args=[pedido.pk])
	resp = client.get(temp_url)
	assert resp.status_code == 302

@pytest.mark.django_db
def test_registrar_pedido(client):
	"""Teste para registrar pedido
	
	:RECEBE:
	:client: Simulacao do cliente na url testada"""
	pedido = Pedido.objects.create(numero =1,mesa_id = 1,garcon_id = 1)
	temp_url = urls.reverse('registrar_pedido', args=[1])
	resp = client.get(temp_url)
	assert resp.status_code == 302


