from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.index, name='resume'),
    path('cripto/', views.cripto, name='cripto'),
    path('my-coins/', views.my_coins, name='my-coins'),
]