from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from catalog.models import Product
from django.urls import reverse, reverse_lazy


class ProductListView(ListView):
    model = Product


class ProductDetail(DetailView):
    model = Product


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


class ProductCreateView(CreateView):
    model = Product
    fields = ('name', 'description', 'category', 'price', 'preview')
    success_url = reverse_lazy('catalog:home')


class ProductUpdateView(UpdateView):
    model = Product
    fields = ('name', 'description', 'category', 'price', 'preview')
    success_url = reverse_lazy('catalog:home')


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:home')


def toggle_stock(request, pk):
    product_item = get_object_or_404(Product, pk=pk)
    if product_item.on_stock:
        product_item.on_stock = False
    else:
        product_item.on_stock = True

    product_item.save()

    return redirect(reverse('catalog:home'))
