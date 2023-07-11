from django.shortcuts import get_object_or_404, render, HttpResponse
from django.views.generic import ListView, DetailView
from .models import Category, Product
from django.http import JsonResponse

def home(request):
    categories = Category.objects.all()

    context = {
        'categories': categories,
    }

    return render(request, 'base.html', {'context': context})

class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        category = get_object_or_404(Category, id=category_id)
        queryset = category.products.all()
        return queryset

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'