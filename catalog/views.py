from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from catalog.models import Product


def home(request):
    product_list = Product.objects.all()
    context = {
        'object_list': product_list,
        'title': 'Каталог товаров'
    }
    return render(request, 'home.html', context)


def product(request, pk):
    # product = Product.objects.get(pk=pk)
    product = get_object_or_404(Product, pk=pk)
    context = {
        'product': product,
        'title': product.name
    }
    return render(request, 'product.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Message from {name}(tel.: {phone}): {message}')
    context = {
        'title': 'Контакты'
    }
    return render(request, 'contacts.html', context)
