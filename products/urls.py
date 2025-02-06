from django.urls import path

from . import views

app_name = 'products'

urlpatterns = [
    path('list/', views.product_list, name='list'),
    path('create/', views.product_create, name='create'),
    path('detail/<int:pk>/', views.product_detail, name='detail'),
    path('delete_list/<int:pk>/', views.delete_list, name='delete_list'),
    path('delete/<int:pk>/', views.product_delete, name='delete'),
    path('update/<int:pk>/', views.product_update, name='update'),
]