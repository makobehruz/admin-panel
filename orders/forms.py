from django import forms

from .models import Order, OrderItem



class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer_name', 'status', 'email', 'phone_number', 'address']
        widgets = {
            'customer_name': forms.TextInput(attrs={'class': 'mt-1 block w-full border-gray-300 rounded-md shadow-sm'}),
            'status': forms.Select(attrs={'class': 'mt-1 block w-full border-gray-300 rounded-md shadow-sm'}),
            'email': forms.EmailInput(attrs={'class': 'mt-1 block w-full border-gray-300 rounded-md shadow-sm'}),
            'phone_number': forms.TextInput(attrs={'class': 'mt-1 block w-full border-gray-300 rounded-md shadow-sm'}),
            'address': forms.Textarea(attrs={'class': 'mt-1 block w-full border-gray-300 rounded-md shadow-sm"', 'rows': 3,}),
        }

class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['product', 'quantity']