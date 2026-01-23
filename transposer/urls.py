from django.urls import path
from .views import calculate_transpose

urlpatterns = [
    path("calculate/", calculate_transpose),
]
