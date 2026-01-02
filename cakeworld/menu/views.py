from django.shortcuts import render
from .models import Product

def product_list(request):
    category = request.GET.get('category')
    sort = request.GET.get('sort')

    products = Product.objects.all()

    if category:
        products = products.filter(category=category)

    if sort == 'low':
        products = products.order_by('price')
    elif sort == 'high':
        products = products.order_by('-price')

    context = {
        'products': products
    }

    return render(request, 'menu/products.html', context)
