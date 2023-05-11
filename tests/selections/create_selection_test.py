import pytest

from tests.factories import AdFactory


@pytest.mark.django_db
def test_create_selection(client, user, auth_token):
    ads = AdFactory.create_batch(4)
    expected_response = {
        'id': 1,
        'name': 'test_selection',
        'owner': user.pk,
        'items': [ad.pk for ad in ads]
    }
    response = client.post(
        '/selection/create/',
        data={
            'name': 'test_selection',
            'owner': user.pk,
            'items': [ad.pk for ad in ads]
        },
        HTTP_AUTHORIZATION=auth_token,
        content_type='application/json'
    )

    assert response.status_code == 201
    assert response.data == expected_response