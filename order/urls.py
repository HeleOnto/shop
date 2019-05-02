from django.urls import path

from . import views

app_name = 'order'
urlpatterns = [
    # catalog/order/
    path('', views.view_cart, name='shopping-cart'),
    # catalog/order/item-added/product_id
    path('item-added/<int:product_id>/', views.add_to_cart, name='item-added'),
    # catalog/order/item-deleted/product_id
    path('item-deleted/<int:product_id>/', views.delete_from_cart, name='item-deleted'),
    # catalog/order/<ref_code>/
    path('<str:ref_code>/', views.checkout, name='checkout'),

]
