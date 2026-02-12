from django.urls import path
from .views import product_list, product_details

# product app routs
urlpatterns = [
    path('', product_list),
    path('product', product_list),
    path('product/<int:pk>/', product_details)
]