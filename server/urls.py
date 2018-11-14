from django.urls import path, include
from django.contrib.auth import views as social_views
from . import views

urlpatterns = [
    # login route
    # path('login/', social_views.LoginView.as_view(), name='login'),
    # logout route
    # path('logout/', social_views.LogoutView.as_view(), name='logout'),
    # auth route
    # path('auth/', include('social_django.urls')),

    # test login route
    path('login/', views.login),
    # test logout route
    path('logout/', views.logout),
    # landing route
    path('', views.landing, name='landing'),
    # dashboard route
    path('dashboard/', views.dashboard, name='dashboard'),
    # superadmin dashboard route
    path('superadmin_dashboard/', views.superadmin_dashboard, name='superadmin_dashboard'),
    # subadmin dashboard route
    path('subadmin_dashboard/', views.subadmin_dashboard, name='subadmin_dashboard'),
    # admin facility route
    path('admin_facility/', views.admin_facility),
    # facility route
    path('facility/', views.facility),
    # view facility route
    path('view_facility/<str:pk>', views.view_facility),
    # add facility route
    path('add_facility/', views.add_facility),
    # edit facility route
    path('edit_facility/<str:pk>', views.edit_facility),
    # equipment route
    path('equipment/', views.equipment),
    # add equipment route
    path('add_equipment/', views.add_equipment),
    # edit equipment route
    path('edit_equipment/<str:pk>', views.edit_equipment),
]