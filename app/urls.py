from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('addrating/', views.add_rating, name='add_rating'),
    path('unsubscribe/', views.unsubscribe, name='unsubscribe'),
]