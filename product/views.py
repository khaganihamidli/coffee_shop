from django.http import JsonResponse, HttpResponse
from .models import Coffee

# Create your views here.

# home end-point
def home(request):
    return HttpResponse("Home page of Coffe shop")

# end-point 1: all coffies
def product_list(request):
    products = list(Coffee.objects.values())
    return JsonResponse(products, safe=False)

# end-point 2: coffee details
def product_details(request, pk):
    try:
        product = Coffee.objects.get(pk=pk)
        data = {
            "id": product.id,
            "name": product.name,
            "price": float(product.price),
            "description": product.description
        }
        return JsonResponse(data)
    except Coffee.DoesNotExist:
        return JsonResponse({"alert_message": "Coffee not found"},status = 404)