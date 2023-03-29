from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('cat/', views.CategoryView.as_view(), name='category'),
    path('cat/<int:pk>/', views.CategoryDetailView.as_view(), name='detail_category'),
    path('ad/', views.AdView.as_view(), name='ad'),
    path('ad/<int:pk>/', views.AdDetailView.as_view(), name='detail_ad'),
]
