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
    return render(request,'categories/list.html', ctx)

def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('categories:list')
        else:
            messages.error(request, 'Fill in the table correctly.')
    form = CategoryForm()
    ctx = {
        'form': form,
    }
    return render(request, 'categories/form.html', ctx)

def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    product_count = Product.objects.filter(category=category).count()
    ctx = {
        'category': category,
        'product_count': product_count,
    }
    return render(request, 'categories/detail.html', ctx)


def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('categories:list')
    return render(request, 'categories/delete.html', {'category': category})


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
        form = CategoryForm(request.POST, request.FILES, instance=category)

        if form.is_valid():
            form.save()
            return redirect('categories:list')
        else:
            messages.error(request, 'Fill in the table correctly.')

    form = CategoryForm(instance=category)

    ctx = {
        'category': category,
        'form': form,
    }
    return render(request, 'categories/form.html', ctx)


