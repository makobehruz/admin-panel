from django.urls import path

from . import views


app_name = 'categories'

urlpatterns = [
    path('list/', views.category_list, name='list'),
    path('create/', views.category_create, name='create'),
    path('search/', views.category_search, name='search'),
    path('detail/<int:pk>/', views.category_detail, name='detail'),
    path('update/<int:pk>/', views.category_update, name='update'),
    path('delete/<int:pk>/', views.category_delete, name='delete'),
    path('delete_list/<int:pk>/', views.delete_list, name='delete_list'),

]