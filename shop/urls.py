from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.product_list, name='products'),
    path('category/<slug:slug>/', views.category_products, name='category_products'),
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),  # ← добавить
    path('index/', views.index, name='index'),
    path('search/', views.search_products, name='search-products'),
]