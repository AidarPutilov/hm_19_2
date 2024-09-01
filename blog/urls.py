from django.urls import path
# from blog.views import (
#     BlogListView,
#     BlogDetailView,
#     BlogCreateView,
#     BlogUpdateView,
#     BlogDeleteView,
#     toggle_stock
# )
from blog.apps import BlogConfig


app_name = BlogConfig.name

urlpatterns = [
    # path('', ProductListView.as_view(), name='home'),
    # path('product/<int:pk>/', ProductDetailView.as_view(), name='view_product'),
    # path('create/', ProductCreateView.as_view(), name='create_product'),
    # path('edit/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),
    # path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),
    # path('activity/<int:pk>/', toggle_stock, name='toggle_stock'),
]