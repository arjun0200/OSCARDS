from django.urls import path
from .views import *

urlpatterns = [
    path('hello/', hello_solid),  # --> /api/hello/
]
