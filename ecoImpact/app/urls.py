from django.urls import path
from .views import get_names


urlpatterns = [
    path('names/', get_names, name='get_names'),
]

















