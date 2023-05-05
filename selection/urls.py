from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListSelectionView.as_view()),
    path('<int:pk>/', views.RetrieveSelectionView.as_view()),
    path('create/', views.CreateSelectionView.as_view()),
    path('<int:pk>/update/', views.UpdateSelectionView.as_view()),
    path('<int:pk>/delete/', views.DestroySelectionView.as_view()),
]
