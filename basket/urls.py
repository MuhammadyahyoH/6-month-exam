from django.urls import path
from . import views

app_name = 'basket'

urlpatterns = [
    path('', views.basket, name='detail'),
    path('add/<int:product_id>/', views.basket_add, name='add'),
    path('remove/<int:product_id>/', views.basket_remove, name='remove'),
    path('update/<int:product_id>/', views.basket_update, name='update'),
    path('checkout/', views.checkout, name='checkout'),
    path('order-success/', views.order_success, name='order_success'),
]