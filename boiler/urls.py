from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('ping/', views.ping, name='ping'),
    path('boiler_gen',views.boiler_gen,name='boiler_gen')
]