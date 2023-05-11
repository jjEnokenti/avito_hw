import pytest

from ads.serializers.ad import AdSerializer


@pytest.mark.django_db
def test_update_ad(client, category, user, ad, auth_token):
    data = {
        'name': 'partial updated name',
        'is_published': True
    }

    matching_data = AdSerializer(ad).data

    response = client.patch(
        f'/ad/{ad.pk}/',
        data=data,
        HTTP_AUTHORIZATION=auth_token,
        content_type='application/json'
    )

    expected_response = {
        'id': ad.pk,
        'name': 'partial updated name',
        'author': user.pk,
        'price': 1000,
        'description': '',
        'image': None,
        'is_published': True,
        'category': category.pk
    }

    assert response.status_code == 200
    assert response.data == expected_response
    assert response.data != matching_data
