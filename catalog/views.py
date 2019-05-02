from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Product, Category, Manufacturer


def product_list(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'product_list.html', {'products': products, 'categories': categories})


def detail(request, category_id, product_id):
    product = get_object_or_404(Product, pk=product_id)
    categories = Category.objects.all()
    return render(request, 'detail.html', {'category_id': category_id, 'product': product,
                                           'product_id': product_id, 'categories': categories})


def sort_by_category(request, category_id):
    categories = Category.objects.all()
    products = Product.objects.filter(category=category_id)
    return render(request, 'sort-by-category.html', {'products': products, 'categories': categories})


def sort_by_manufacturer(request, manufacturer_id):
    categories = Category.objects.all()
    product = get_list_or_404(Product, manufacturer=manufacturer_id)
    return render(request, 'sort-by-manufacturer.html', {'product': product, 'categories': categories})
