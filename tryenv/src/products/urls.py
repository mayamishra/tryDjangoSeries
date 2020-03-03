from django.urls import path
from products.views import (
    product_create_view,
    product_detail_view,
    product_delete_view,
    product_update_view,
    render_initial_data,
    dynamic_lookup_view,
    product_list_view,
)

urlpatterns = [
    path('',product_list_view, name='product-list'),
    path('/<int:id>/update/',product_update_view, name='product-update'),
    path('/<int:id>/delete',product_delete_view, name='product-delete'),
    path('/create',product_create_view,name='product-list'),
    
    path('/<int:id>/',product_detail_view, name='product-detail')
]