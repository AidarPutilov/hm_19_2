from django.urls import path
from catalog.views import contacts, ProductListView, ProductDetail
from catalog.apps import CatalogConfig


app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', contacts, name='contacts'),
    path('product/<int:pk>', ProductDetail.as_view(), name='product'),
]