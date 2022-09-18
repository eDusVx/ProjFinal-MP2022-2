import pytest
from ristorante import settings
from django.contrib.auth import get_user_model


@pytest.fixture(scope='session')
def django_db_setup():
    settings.DATABASES= {
    'tests': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': settings.os.path.join(settings.BASE_DIR, 'yourdatabasename.db'),
    }
}

@pytest.fixture
def user_data():
	return {'username': 'user_name', 'password': 'user_pass543'}


@pytest.fixture
def create_test_user(user_data):
	user_model = get_user_model()
	test_user = user_model.objects.create_user(**user_data)
	test_user.set_password(user_data.get('password'))
	return test_user


@pytest.fixture
def authenticated_user(client, user_data):
	user_model = get_user_model()
	test_user = user_model.objects.create_user(**user_data)
	test_user.set_password(user_data.get('password'))
	test_user.save()
	client.login(**user_data)
	return test_user

