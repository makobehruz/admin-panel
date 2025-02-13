from django.shortcuts import render
from django.db.models import Count

from orders.models import Order
from categories.models import Category


def home(request):
    categories = Category.objects.annotate(product_count=Count('products'))
    orders = Order.objects.all()
    total_price = Order.get_all_orders_total()
    ctx = {
        'orders': orders,
        'total_price': total_price,
        'categories': categories,
        }
    return render(request,'dashboard/index.html', ctx)



