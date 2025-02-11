from django import forms
from django.core.exceptions import ValidationError

from .models import Product


class ProductForm(forms.ModelForm):
    image = forms.ImageField(required=False, widget=forms.FileInput(attrs={
        'class': 'mt-1 block w-full'
    }))

    def clean_name(self):
        names = self.cleaned_data['name'].split()
        for name in names:
            if not name.isalpha():
                raise ValidationError('The product name must consist of letters.')
        return self.cleaned_data['name']

    class Meta:
        model = Product
        fields = ['name', 'category', 'price', 'desc', 'image']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500'
            }),
            'category': forms.Select(attrs={
                'class': 'mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500'
            }),
            'desc': forms.Textarea(attrs={
                'class': 'mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500'
            }),
        }
