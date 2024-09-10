from django.urls import path
from catalog.views import (ProductListView,
                           ProductDetailView,
                           ProductCreateView,
                           ProductUpdateView,
                           ProductDeleteView,
                           toggle_stock,
                           ContactTemplateView)
from catalog.apps import CatalogConfig


app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='view_product'),
    path('create/', ProductCreateView.as_view(), name='create_product'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),
    path('activity/<int:pk>/', toggle_stock, name='toggle_stock'),
    path("contacts/", ContactTemplateView.as_view(template_name="contacts.html"), name='contacts'),
]