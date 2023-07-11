from django.urls import path
from .views import home, ProductListView, ProductDetailView

app_name = 'store'

urlpatterns = [
    path('', home, name='home'),
    path('categories/<int:category_id>/products/', ProductListView.as_view(), name='product_list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
]