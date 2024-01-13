from django.urls import path
from . import views

# URL patterns for the TechColl app
urlpatterns = [
    # Home page
    path('', views.home, name='techcoll-home'),
    # Courses page
    path('courses/', views.courses, name='techcoll-courses'),
    # Costs page
    path('costs/', views.costs, name='techcoll-costs'),
    # Contact page
    path('contact/', views.contact, name='techcoll-contact'),
]

