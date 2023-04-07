from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListUserView.as_view(), name='all_users'),
    path('create/', views.CreateUserView.as_view(), name='create_user'),
    path('<int:pk>/', views.DetailUserView.as_view(), name='detail_view'),
    path('<int:pk>/update/', views.UpdateUserView.as_view(), name='update_user'),
    path('<int:pk>/delete/', views.DeleteUserView.as_view(), name='delete_user'),
]
