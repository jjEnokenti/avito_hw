import pytest

from ads.serializers.ad import AdCreateSerializer


@pytest.mark.django_db
def test_update_ad(client, ad, auth_token):

    response = client.delete(
        f'/ad/{ad.pk}/',
        HTTP_AUTHORIZATION=auth_token,
    )

    assert response.status_code == 204
    assert response.data is None
