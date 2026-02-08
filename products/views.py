from django.shortcuts import render, redirect
from django.http import HttpResponse
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
    products = Product.objects.all()

    return render(request, 'products/product_list.html', {'products':products})

def create_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProductForm()

    return render(request,
                 'products/create_product.html',
                 {'form':form})
