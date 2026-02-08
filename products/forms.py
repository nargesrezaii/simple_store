from django import forms
from .models import Category, Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'stock', 'category']

class CategoryForm(forms.ModelForm):
    class meta:
        model = Category
        fields = ['name']