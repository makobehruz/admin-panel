from django.db import models
from django.urls import reverse
from products.models import Product


class Order(models.Model):
    STATUS_CHOICES = [
        ('pd', 'Pending'),
        ('pg', 'Processing'),
        ('shd', 'Shipped'),
        ('dd', 'Delivered'),
        ('cd', 'Cancelled'),
    ]

    customer_name = models.CharField(max_length=200)
    status = models.CharField(max_length=3, choices=STATUS_CHOICES, default='pd')
    email = models.EmailField()
    phone_number = models.CharField(max_length=13)
    address = models.TextField()
    created_at = models.DateField(auto_now_add=True)

    products = models.ManyToManyField(Product, through='OrderItem', related_name='orders')

    def get_detail_url(self):
        return reverse('orders:detail', args=[self.pk])

    def get_delete_url(self):
        return reverse('orders:delete', args=[self.pk])

    def get_update_url(self):
        return reverse('orders:update', args=[self.pk])

    def get_total_price(self):
        total = sum(item.quantity * item.product.price for item in self.order_items.all())
        return total

    def __str__(self):
        return f"Order {self.pk} - {self.customer_name}"

    @staticmethod
    def get_all_orders_total():
        orders = Order.objects.all()
        total = sum(order.get_total_price() for order in orders)
        return total

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items')
    quantity = models.PositiveIntegerField(default=1)

    def get_price(self):
        return self.quantity * self.product.price

    def __str__(self):
        return f"{self.quantity} {self.product.name}"

    def get_order_item_delete_url(self):
        return reverse('orders:order_item_delete', args=[self.pk])
