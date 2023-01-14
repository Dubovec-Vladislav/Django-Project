from django.urls import path, include
from .views import *

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('about/', about, name="about"),
    path('services/', include('services.urls')),
    path('blog/', include('blog.urls')),
]
