from django.urls import path

from ads.views import category

urlpatterns = [
    path('', category.CategoryListView.as_view(), name='all_categories'),
    path('create/', category.CategoryCreateView.as_view(), name='create_category'),
    path('<int:pk>/', category.CategoryRetrieveView.as_view(), name='detail_category'),
    path('<int:pk>/update/', category.CategoryUpdateView.as_view(), name='update_category'),
    path('<int:pk>/delete/', category.CategoryDestroyView.as_view(), name='delete_category'),
]
