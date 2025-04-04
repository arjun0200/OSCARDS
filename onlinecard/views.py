from django.http import JsonResponse
from rest_framework.decorators import api_view

@api_view(["GET"])
def hello_solid(request):
    return JsonResponse({"message": "Hello from Django!"})
