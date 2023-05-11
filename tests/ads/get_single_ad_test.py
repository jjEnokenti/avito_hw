import pytest

from ads.serializers.ad import AdSerializer
from tests.factories import AdFactory


@pytest.mark.django_db
def test_get_single_ad(client, auth_token):
    ad = AdFactory.create()

    expected_response = AdSerializer(ad).data

    response = client.get(f'/ad/{ad.pk}/', HTTP_AUTHORIZATION=auth_token)

    assert response.status_code == 200
    assert response.data == expected_response
