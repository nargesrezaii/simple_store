from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('products/create/',views.create_product,name="product_create"),
    path('categories/create/',views.create_category, name="create_category"),
    path('categories/',views.category_list, name="category_list"),
    path('products/', views.product_list, name="product_list"),
    path('products/<int:pk>/', views.product_detail, name="product_detail"),
    path('products/update/<int:pk>/', views.product_update, name="product_update"),
]