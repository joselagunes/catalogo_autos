from django.urls import path
from . import views

urlpatterns = [
    path('', views.catalogo, name='catalogo'),
    path('<slug:category_slug>/', views.catalogo, name='cars_by_category'),
    path('<slug:category_slug>/<slug:car_slug>/', views.car_detail, name='car_detail'),  
]

