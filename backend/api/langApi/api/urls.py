from django.urls import path
from . import views

urlpatterns = [
    path('translate/', views.translate),
    path('detect/', views.detect),
]