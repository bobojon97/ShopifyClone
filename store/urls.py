from django.urls import path
from .views import CategoryListView, ProductDetailView, home

app_name = 'store'

urlpatterns = [
    path('', home, name='home'),
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
]