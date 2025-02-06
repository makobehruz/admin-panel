from django import forms
from django.core.exceptions import ValidationError

from categories.models import Category


class ProductForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500'
    }))
    category = forms.ModelChoiceField(queryset=Category.objects.all(), widget=forms.Select(attrs={
        'class': 'mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500'
    }))
    price = forms.DecimalField(max_digits=10, decimal_places=2, widget=forms.NumberInput(attrs={
        'class': 'mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500'
    }))
    desc = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500'
    }))
    image = forms.ImageField(widget=forms.FileInput(attrs={
        'class': 'mt-1 block w-full'
    }))

    def clean_name(self):
        names = self.cleaned_data['name'].split()
        for name in names:
            if not name.isalpha():
                raise ValidationError('The category name must consist of letters.')
        return self.cleaned_data['name']
