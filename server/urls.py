from django.urls import path
from . import views

urlpatterns = [
    # home route
    path('home/', views.home),
    # facility route
    path('facility/', views.facility),
    # equipment route
    path('equipment/', views.equipment)
]