from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('cat/', views.CategoryView.as_view(), name='category'),
    path('cat/<int:pk>/', views.CategoryDetailView.as_view(), name='detail_category'),
    path('cat/<int:pk>/update/', views.CategoryUpdateView.as_view(), name='update_category'),
    path('cat/<int:pk>/delete/', views.CategoryDeleteView.as_view(), name='delete_category'),
    path('ad/', views.AdView.as_view(), name='ad'),
    path('ad/<int:pk>/', views.AdDetailView.as_view(), name='detail_ad'),
    path('ad/<int:pk>/update/', views.AdUpdateView.as_view(), name='update_ad'),
    path('ad/<int:pk>/delete/', views.AdDeleteView.as_view(), name='delete_ad'),

]
