from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from catalog.forms import ProductForm
from catalog.models import Product
from django.urls import reverse, reverse_lazy


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    # fields = ('name', 'description', 'category', 'price', 'preview')
    success_url = reverse_lazy('catalog:home')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    # fields = ('name', 'description', 'category', 'price', 'preview')
    success_url = reverse_lazy('catalog:home')

    def get_success_url(self):
        return reverse('catalog:view_product', args=[self.kwargs.get('pk')])


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:home')


class ContactTemplateView(TemplateView):
    pass


def toggle_stock(request, pk):
    product_item = get_object_or_404(Product, pk=pk)
    product_item.in_stock = not product_item.in_stock
    product_item.save()
    return redirect(reverse('catalog:home'))


# def contacts(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         phone = request.POST.get('phone')
#         message = request.POST.get('message')
#         print(f'Message from {name}(tel.: {phone}): {message}')
#     context = {
#         'title': 'Контакты'
#     }
#     return render(request, 'contacts.html', context)
