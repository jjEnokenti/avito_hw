import pytest


@pytest.mark.django_db
def test_create_ad(client, ad, auth_token):
    data = {
        'name': ad.name,
        'author': ad.author.pk,
        'price': ad.price,
        'category': ad.category.pk
    }
    response = client.post(
        '/ad/',
        data=data,
        HTTP_AUTHORIZATION=auth_token,
        content_type='application/json'
    )

    expected_response = {
        'id': response.data['id'],
        'name': ad.name,
        'author': ad.author.pk,
        'price': 1000,
        'description': '',
        'image': None,
        'is_published': False,
        'category': ad.category.pk
    }

    assert response.status_code == 201
    assert response.data == expected_response
