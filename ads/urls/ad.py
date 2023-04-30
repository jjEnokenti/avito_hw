from rest_framework import routers

from ads.views import ad

router = routers.SimpleRouter()
router.register('', ad.AdViewSet)

urlpatterns = [

]

urlpatterns += router.urls
