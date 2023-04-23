from django.urls import path

from . import views

urlpatterns = [
    path('', views.UserListView.as_view(), name='all_users'),
    path('create/', views.UserCreateView.as_view(), name='create_user'),
    path('<int:pk>/', views.UserRetrieveView.as_view(), name='detail_view'),
    path('<int:pk>/update/', views.UserUpdateView.as_view(), name='update_user'),
    path('<int:pk>/delete/', views.UserDestroyView.as_view(), name='delete_user'),
]
