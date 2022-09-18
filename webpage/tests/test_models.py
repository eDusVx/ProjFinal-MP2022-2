import pytest
from webpage.models import Garcon, Mesa, Pedido

@pytest.mark.django_db
def test_model_garcom():
        nome_completo = Garcon.objects.create(
            nome_completo = 'RENATO SILVA XAVIER',
            email = 'duhauhd@gmail.com',
            password =  '123321')
        assert nome_completo.nome_completo == 'RENATO SILVA XAVIER'