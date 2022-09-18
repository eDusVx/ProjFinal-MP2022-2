from lzma import FORMAT_AUTO
from statistics import quantiles
import pytest
from webpage.models import Garcon, Mesa, Ingrediente, Prato, Pedido, pedido_has_prato, prato_has_ingrediente
import tempfile

@pytest.mark.django_db
def test_model_garcom():
    """Teste para retornar o nome do garcom"""
    garcon = Garcon.objects.create(
        nome_completo = 'RENATO SILVA XAVIER',
        email = 'duhauhd@gmail.com',
        password =  '123321')
    assert garcon.nome_completo == 'RENATO SILVA XAVIER'

@pytest.mark.django_db
def test_model_mesa():
    """Teste para retornar o numero da mesa"""
    garcon = Garcon.objects.create(
        nome_completo = 'RENATO SILVA XAVIER',
        email = 'duhauhd@gmail.com',
        password =  '123321')
        
    mesa = Mesa.objects.create(
        numero = 5,
        quantidade = 2,
        garcon_responsavel = garcon)
    assert mesa.numero == 5

@pytest.mark.django_db
def test_model_ingrediente():
    """Teste para retornar o nome do ingrediente"""
    ingrediente = Ingrediente.objects.create(
        nome = 'PAO',
        quantidade = '100',
        valor_energetico = 100,
        carboidratos = 100,
        proteinas = 200,
        gorduras = 100,
        fibra_alimentar = 100,
        sodio = 0.98,
        acucares = 0.8,
        colesterol = 1.56
    )
    assert ingrediente.nome == 'PAO'

@pytest.mark.django_db
def test_model_prato():
    """Teste para retornar o nome do prato"""

    ingrediente = Ingrediente.objects.create(
        nome = 'PAO',
        quantidade = '100',
        valor_energetico = 100,
        carboidratos = 100,
        proteinas = 200,
        gorduras = 100,
        fibra_alimentar = 100,
        sodio = 0.98,
        acucares = 0.8,
        colesterol = 1.56
    ) 

    prato = Prato.objects.create(
        nome = 'HAMBURGER',
        foto = tempfile.NamedTemporaryFile(suffix=".jpg").name,
        preco = 40,
        tipo = 1)

    prato_has_ingrediente.objects.create(
        prato = prato,
        ingrediente = ingrediente,
        quantidade = 5
    ) 

    assert prato.nome == 'HAMBURGER'

@pytest.mark.django_db
def test_model_pedido():
    """Teste para retornar o nome do garçom do pedido"""
    garcon = Garcon.objects.create(
        nome_completo = 'RENATO SILVA XAVIER',
        email = 'duhauhd@gmail.com',
        password =  '123321')
        
    mesa = Mesa.objects.create(
        numero = 5,
        quantidade = 2,
        garcon_responsavel = garcon)

    pedido =Pedido.objects.create(
        numero= '1',
        mesa_id=mesa.id,
        garcon_id =garcon.id
    )

    assert str(pedido.garcon) == 'RENATO SILVA XAVIER'

@pytest.mark.django_db
def test_model_pedido_has_ingrediente():
    """Teste para retornar o ingrediente da tabela pedido_has_ingrediente"""
    garcon = Garcon.objects.create(
        nome_completo = 'RENATO SILVA XAVIER',
        email = 'duhauhd@gmail.com',
        password =  '123321')

    mesa = Mesa.objects.create(
        numero = 5,
        quantidade = 2,
        garcon_responsavel = garcon)

    prato = Prato.objects.create(
        nome = 'HAMBURGER',
        foto = tempfile.NamedTemporaryFile(suffix=".jpg").name,
        preco = 40,
        tipo = 1)

    ingrediente = Ingrediente.objects.create(
        nome = 'PAO',
        quantidade = '100',
        valor_energetico = 100,
        carboidratos = 100,
        proteinas = 200,
        gorduras = 100,
        fibra_alimentar = 100,
        sodio = 0.98,
        acucares = 0.8,
        colesterol = 1.56
    ) 
    prato_has_ingrediente1=prato_has_ingrediente.objects.create(
        prato = prato,
        ingrediente = ingrediente,
        quantidade = 5
    ) 
    pedido =Pedido.objects.create(
        numero= '1',
        mesa_id=mesa.id,
        garcon_id =garcon.id
    )

    assert prato_has_ingrediente1.ingrediente == ingrediente

@pytest.mark.django_db
def test_model_pedido_has_prato():
    """Teste da tabela pedido_has_prato"""
    garcon = Garcon.objects.create(
        nome_completo = 'RENATO SILVA XAVIER',
        email = 'duhauhd@gmail.com',
        password =  '123321')

    mesa = Mesa.objects.create(
        numero = 5,
        quantidade = 2,
        garcon_responsavel = garcon)

    prato = Prato.objects.create(
        nome = 'HAMBURGER',
        foto = tempfile.NamedTemporaryFile(suffix=".jpg").name,
        preco = 40,
        tipo = 1)

    ingrediente = Ingrediente.objects.create(
        nome = 'PAO',
        quantidade = '100',
        valor_energetico = 100,
        carboidratos = 100,
        proteinas = 200,
        gorduras = 100,
        fibra_alimentar = 100,
        sodio = 0.98,
        acucares = 0.8,
        colesterol = 1.56
    ) 
    pedido =Pedido.objects.create(
        numero= '1',
        mesa_id=mesa.id,
        garcon_id =garcon.id
    )
    pedido_has_prato1=pedido_has_prato.objects.create(
        prato = prato,
        pedido = pedido,
        quantidade = 5
    ) 

    assert pedido_has_prato1.pedido == pedido

