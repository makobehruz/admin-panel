from django.shortcuts import render

from orders.forms import Order


def home(request):
    orders = Order.objects.all()
    ctx = {'orders': orders}
    return render(request,'dashboard/index.html', ctx)



