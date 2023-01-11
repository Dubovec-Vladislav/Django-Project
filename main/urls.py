from django.urls import path, include
from .views import *

urlpatterns = [
    path('', main, name="home"),
    path('about/', about, name="about"),
    path('services/', include('services.urls')),
]
