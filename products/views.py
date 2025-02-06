from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from categories.models import Category
from .models import Product
from .forms import ProductForm


def product_list(request):
    search_query = request.GET.get('search', '')
    selected_category = request.GET.get('category', '')
    sort_by = request.GET.get('sort_by', 'high')

    products = Product.objects.all()

    if search_query:
        products = products.filter(name__icontains=search_query)

    if selected_category:
        products = products.filter(category_id=selected_category)

    if sort_by == 'low':
        products = products.order_by('price')
    elif sort_by == 'high':
        products = products.order_by('-price')
    else:
        products = products.order_by('name')

    categories = Category.objects.all()
    ctx = {
        'products': products,
        'categories': categories,
        'search': search_query,
        'selected_category': selected_category,
        'sort_by': sort_by,
    }
    return render(request, 'products/list.html', ctx)

def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            Product.objects.create(
                name = form.cleaned_data['name'],
                category = form.cleaned_data['category'],
                price = form.cleaned_data['price'],
                desc = form.cleaned_data['desc'],
                image = request.FILES['image'],
            )
            return redirect('products:list')
        else:
            messages.error(request, 'The category name must consist of letters.')
    else:
        form = ProductForm()
    return render(request,'products/form.html', {'form': form })

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    ctx = {'product': product }
    return render(request, 'products/detail.html', ctx)

def delete_list(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request,'products/delete.html', {'product': product })

def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('products:list')

def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product.name = form.cleaned_data['name']
            product.category = form.cleaned_data['category']
            product.price = form.cleaned_data['price']
            product.desc = form.cleaned_data['desc']
            product.image = request.FILES['image']
            product.save()
            return redirect('products:list')
        else:
            messages.error(request, 'The category name must consist of letters.')
    else:
        form = ProductForm(initial={
            'name': product.name,
            'category': product.category,
            'price': product.price,
            'desc': product.desc,
            'image': product.image,
        })
    return render(request,'products/form.html', {'form': form })

