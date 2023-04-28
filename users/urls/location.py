from rest_framework import routers

from users.views import location

router = routers.SimpleRouter()
router.register('', location.LocationViewSet)

urlpatterns = [

]

urlpatterns += router.urls
