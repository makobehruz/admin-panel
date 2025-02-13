from django import forms
from django.core.exceptions import ValidationError
from .models import Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'desc', 'image']

    image = forms.ImageField(required=False, widget=forms.FileInput(attrs={
        'class': 'block text-sm font-medium text-gray-700',
    }))

    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500',
    }))

    desc = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500',
    }))

    def clean_name(self):
        names = self.cleaned_data['name'].split()
        for name in names:
            if not name.isalpha():
                raise ValidationError('The category name must consist of letters.')
        return self.cleaned_data['name']


