from django.urls import path  # Removed the trailing comma
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Route for the home page
]
