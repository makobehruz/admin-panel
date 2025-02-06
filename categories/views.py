from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from products.models import Product
from .models import Category
from .forms import CategoryForm


def category_list(request):
    categories = Category.objects.all()
    ctx = {
        'categories': categories,
        'product_count': Product.objects.count(),
    }
    for category in categories:
        category.product_count = Product.objects.filter(category=category).count()
    return render(request,'categories/list.html', ctx)

def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            Category.objects.create(
                name = form.cleaned_data['name'],
                desc = form.cleaned_data['desc'],
                image = request.FILES['image'],
            )
            return redirect('categories:list')
        else:
            messages.error(request, 'The category name must consist of letters.')
    else:
        form = CategoryForm()
    return render(request,'categories/form.html', {'form': form})

def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    product_count = Product.objects.filter(category=category).count()
    ctx = {
        'category': category,
        'product_count': product_count,
    }
    return render(request, 'categories/detail.html', ctx)


def delete_list(request, pk):
    category = get_object_or_404(Category, pk=pk)
    return render(request,'categories/delete.html', {'category': category})

def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('categories:list')

def category_search(request):
    search = request.GET.get('search', '')
    categories = Category.objects.all()
    if search:
        categories = categories.filter(name__icontains = search)
    ctx = {
        'search': search,
        'categories': categories,
    }
    return render(request,'categories/list.html', ctx)


def category_update(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            category.name = form.cleaned_data['name']
            category.desc = form.cleaned_data['desc']
            category.image = request.FILES['image']
            category.save()
            return redirect('categories:list')
        else:
            messages.error(request, 'The category name must consist of letters.')
    form = CategoryForm(initial={
    'name': category.name,
    'desc': category.desc,
    'image': category.image
        })
    ctx = {
        'category': category,
        'form': form,
    }
    return render(request,'categories/form.html', ctx)

