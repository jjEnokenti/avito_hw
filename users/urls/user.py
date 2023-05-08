from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.views import user

router = routers.SimpleRouter()
router.register('', user.UserViewSet)

urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('register/', user.CreateUserView.as_view()),
]

urlpatterns += router.urls
