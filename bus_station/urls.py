from django.urls import path
from . import views

# URL patterns for the bus_station app
urlpatterns = [
    # Main page
    path('', views.main, name='bus_station-main'),
    # Routes page
    path('routes/', views.routes, name='bus_station-routes'),
    # Prices page
    path('prices/', views.prices, name='bus_station-prices'),
    # Contacts page
    path('contacts/', views.contacts, name='bus_station-contacts'),
]
