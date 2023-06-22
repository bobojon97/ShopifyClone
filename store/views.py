from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, DetailView
from .models import Category, Product


def home(request):
    # Получаем все товары из базы данных
    products = Product.objects.all()

    return render(request, 'base.html', {'products': products})

class CategoryListView(ListView):
    model = Category
    template_name = 'category_list.html'
    context_object_name = 'categories'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'
