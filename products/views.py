from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

import products
from .models import Product, Category
from .forms import CategoryForm, ProductForm

def home(request):
    return HttpResponse("Home Page")

def category_list(request):
    categories = Category.objects.all()
  
    return render(request, 'products/category_list.html', {'categories':categories})

def create_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
        
    return render(request,
                  "products/create_category.html",
                 {'form': form})

def product_list(request):
    products = Product.objects.select_related('category')
    categories = Category.objects.all()
    
    category_id = request.GET.get('category')
    
    if category_id:
        category_id = int(category_id)
        products = products.filter(category_id=category_id)
      
    context = {'products':products, 'categories': categories, 'selected_category': category_id,}

    return render(request, 'products/product_list.html', context)

def product_detail(request, pk):
    product = get_object_or_404(
        Product.objects.select_related('category'),
        pk = pk 
    )
    
    return render(request, 'products/product_detail.html', {'product':product})

def create_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()

    return render(request,
                 'products/create_product.html',
                 {'form':form})

def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)

        if form.is_valid():
            form.save()
            return redirect('product_detail', pk=product.pk)

    else:
        form = ProductForm(instance=product)
        
    return render(request, 'products/product_form.html', {'form': form})