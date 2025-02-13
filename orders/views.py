from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect, reverse

from .models import Order, OrderItem
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
    return render(request, 'orders/delete.html', {'order': order})


def order_update(request, pk):
    order = get_object_or_404(Order, pk=pk)
    order_items = order.order_items.all()
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            for item in order_items:
                quantity_field = f'quantity_{item.pk}'
                price_field = f'price_{item.pk}'
                if quantity_field in request.POST and price_field in request.POST:
                    new_quantity = int(request.POST[quantity_field])
                    new_price = float(request.POST[price_field])
                    item.quantity = new_quantity
                    item.product.price = new_price
                    item.product.save()
                    item.save()
            return redirect('orders:list')
    else:
        form = OrderForm(instance=order)
    return render(request, 'orders/form.html', {
        'form': form,
        'order_items': order_items,
        'order': order,
    })

def order_item_delete(request, pk):
    order_item = get_object_or_404(OrderItem, pk=pk)
    order_id = order_item.order.id
    order_item.delete()
    return redirect(reverse('orders:update', args=[order_id]))