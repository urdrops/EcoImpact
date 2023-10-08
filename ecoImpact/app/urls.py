from django.urls import path
from .views import get_models


urlpatterns = [
    path('names/', get_models, name='get_names'),
]
