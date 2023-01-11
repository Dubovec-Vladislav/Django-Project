from django.urls import path
from .views import *

urlpatterns = [
    path('food/', food, name="food"),
    path('fashion/', fashion, name="fashion"),
    path('booking/', booking, name="booking"),
    path('marketing/', marketing, name="marketing"),
    path('design/', design, name="design"),
    path('making-food/', making_food, name="making-food"),
]
