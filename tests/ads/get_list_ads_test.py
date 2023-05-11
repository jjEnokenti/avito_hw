import pytest

from ads.serializers.ad import AdSerializer
from tests.factories import AdFactory


@pytest.mark.django_db
def test_get_list_ad(client):
    ads = AdFactory.create_batch(10)
    sorted_ads = sorted(ads, key=lambda ad: (-ad.price, ad.name))

    expected_response = {
        'count': 10,
        'next': None,
        'previous': None,
        'results': AdSerializer(sorted_ads, many=True).data
    }
    response = client.get('/ad/')

    assert response.status_code == 200
    assert len(response.data['results']) == 10
    assert response.data == expected_response
