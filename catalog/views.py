from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from catalog.models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'home.html'


class ProductDetail(DetailView):
    model = Product
    template_name = 'product.html'


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
