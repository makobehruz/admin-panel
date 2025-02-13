from django.urls import path

from . import views


app_name = 'orders'

urlpatterns = [
    path('list/', views.order_list, name='list'),
    path('detail/<int:pk>/', views.order_detail, name='detail'),
    path('delete/<int:pk>/', views.order_delete, name='delete'),
    path('order_item_delete/<int:pk>/', views.order_item_delete, name='order_item_delete'),
    path('update/<int:pk>/', views.order_update, name='update'),
]