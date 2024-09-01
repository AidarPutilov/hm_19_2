from django.urls import path
from catalog.views import (contacts,
                           ProductListView,
                           ProductDetail,
                           ProductCreateView,
                           ProductUpdateView,
                           ProductDeleteView, toggle_stock)
from catalog.apps import CatalogConfig


app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', contacts, name='contacts'),
    path('product/<int:pk>/', ProductDetail.as_view(), name='view_product'),
    path('create/', ProductCreateView.as_view(), name='create_product'),
    path('edit/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),
    path('activity/<int:pk>/', toggle_stock, name='toggle_stock'),
]