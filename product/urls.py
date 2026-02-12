from django.urls import path
from .views import home, product_list, product_details

# product app routs
urlpatterns = [
    path('', home, name="home"),
    path('products', product_list, name="products"),
    path('products/<int:pk>/', product_details, name="details"),
]