import pytest


@pytest.fixture()
@pytest.mark.django_db
def auth_token(client, django_user_model):
    username = 'test_user'
    password = '1234'
    email = 'test@test.com'
    birth_date = '2000-11-11'

    django_user_model.objects.create_user(
        username=username,
        password=password,
        email=email,
        birth_date=birth_date,
        role='admin'
    )

    response = client.post(
        '/user/login/',
        data={
            'username': username,
            'password': password
        },
        content_type='application/json'
    )

    token = f'Bearer {response.data["access"]}'

    return token

