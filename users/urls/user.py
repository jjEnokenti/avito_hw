from rest_framework import routers

from users.views import user

router = routers.DefaultRouter()
router.register('', user.UserViewSet)


urlpatterns = [

]

urlpatterns += router.urls
