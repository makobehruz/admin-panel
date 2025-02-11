from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect

from .models import Order
from .forms import OrderForm


def order_list(request):
    orders = Order.objects.all()
    search = request.GET.get('search', '')
    status = request.GET.get('status', '')
    if search:
        orders = orders.filter(customer_name__icontains = search)

    if status:
        orders = orders.filter(status=status)

    ctx = {
        'orders': orders,
        'search': search,
        'status': status,
    }
    return render(request,'orders/list.html', ctx)

def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)
    ctx = {'order': order}
    return render(request,'orders/detail.html', ctx)

def order_delete(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('orders:list')
    return render(request, 'orders/delete.html')

def order_update(request, pk):
    order = get_object_or_404(Order, pk=pk)
    order_items = order.order_items.all()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order.customer_name = form.cleaned_data['customer_name']
            order.status = form.cleaned_data['status']
            order.email = form.cleaned_data['email']
            order.phone_number = form.cleaned_data['phone_number']
            order.address = form.cleaned_data['address']
            order.save()
            return redirect('orders:list')
    else:
        form = OrderForm(initial={
            'customer_name': order.customer_name,
            'status': order.status,
            'email': order.email,
            'phone_number': order.phone_number,
            'address': order.address,
        })
    return render(request, 'orders/form.html', {'form': form, 'order_items': order_items, 'order': order})

