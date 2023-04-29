from rest_framework import routers

from ads.views import category

router = routers.SimpleRouter()
router.register('', category.CategoryViewSet)

urlpatterns = [

]

urlpatterns += router.urls
