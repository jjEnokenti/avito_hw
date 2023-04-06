from django.urls import path

from ads.views import category

urlpatterns = [
    path('', category.CategoryView.as_view(), name='category'),
    path('create/', category.CategoryCreateView.as_view(), name='create_category'),
    path('<int:pk>/', category.CategoryDetailView.as_view(), name='detail_category'),
    path('<int:pk>/update/', category.CategoryUpdateView.as_view(), name='update_category'),
    path('<int:pk>/delete/', category.CategoryDeleteView.as_view(), name='delete_category'),
]
