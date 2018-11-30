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
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    # admin facility route
    path('admin_facility/', views.admin_facility),
    # admin reservation route
    path('admin_reservation/', views.admin_reservation),
    # admin facility route
    path('admin_equipment/', views.admin_equipment),
    # admin reservation route
    # facility route
    path('facility/', views.facility),
    # view facility route
    path('view_facility/<str:pk>', views.view_facility),
    # view admin facility route
    path('view_admin_facility/<str:pk>', views.view_admin_facility),
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
    # view admin facility route
    path('view_admin_equipment/<str:pk>', views.view_admin_equipment),
    # apply reservation route
    path('apply_reservation/<str:pk>', views.apply_reservation),
]