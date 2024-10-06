from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:amount>/', views.calculate, name='tax'),
    path('taxrate/',views.showtax, name='tax_rate'),
]