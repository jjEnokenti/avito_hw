
from django.urls import path

from ads.views import ad

urlpatterns = [
    path('', ad.AdView.as_view(), name='all_ads'),
    path('create/', ad.AdCreateView.as_view(), name='create_ad'),
    path('<int:pk>/', ad.AdRetrieveView.as_view(), name='detail_ad'),
    path('<int:pk>/update/', ad.AdUpdateView.as_view(), name='update_ad'),
    path('<int:pk>/delete/', ad.AdDeleteView.as_view(), name='delete_ad'),
    path('<int:pk>/upload_image/', ad.AdUploadImageView.as_view(), name='upload_image'),
]
