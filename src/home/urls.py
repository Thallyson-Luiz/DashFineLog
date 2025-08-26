from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.index, name='resume'),
    path('cripto', views.cripto, name='cripto'),
]