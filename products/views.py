from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product, Category

def home(request):
    return HttpResponse("Home Page")

def category_list(request):
    categories = Category.objects.all()
  
    return render(request, 'products/category_list.html', {'categories':categories})

def create_category(request):
    if request.method == "POST":
        name = request.POST.get('name')

        if not name:
            return render(request, 'products/create_category.html', {'error':'Category name is required.'})
        
        Category.objects.create(name=name)
        return redirect('category_list')

    return render(request, "products/create_category.html")

def create_product(request):
    categories = Category.objects.all()
    
    if not categories.exists():
        return HttpResponse(
            "You must create categories before adding products.",
            status=400
        )

    if request.method == "POST":
        category_id = request.POST.get('category')
        category = Category.objects.get(id=category_id)

        Product.objects.create(
            name = request.POST.get('name'),
            price = request.POST.get('price'),
            description=request.POST.get('description'),
            stock=request.POST.get('stock'),
            category=category
            )
        
        return redirect('home')

    return render(request,
                 'products/create_product.html',
                 {'categories':categories})
