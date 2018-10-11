from django.urls import path
from . import views

urlpatterns = [
    # home route
    path('', views.landing),
    # facility route
    path('facility/', views.facility),
    # add facility route
    path('add_facility', views.add_facility),
    # equipment route
    path('equipment/', views.equipment),
]