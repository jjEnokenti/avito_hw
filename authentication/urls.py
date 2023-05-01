from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

from .views import CreateUserView

urlpatterns = [
    # path('login/', views.ObtainAuthToken.as_view()),
    # path('logout/', LogoutView.as_view()),
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('register/', CreateUserView.as_view()),
]
