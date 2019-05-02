from django.urls import path, include

from . import views

app_name = 'catalog'
urlpatterns = [
    # catalog/
    path('', views.product_list, name='product_list'),
    # catalog/1/item/1/
    path('<int:category_id>/item/<int:product_id>/', views.detail, name='detail'),
    # catalog/1/
    path('<int:category_id>/', views.sort_by_category, name='sort-by-category'),
    # catalog/order/
    path('order/', include('order.urls')),
]
