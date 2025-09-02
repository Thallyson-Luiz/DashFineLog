from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.index, name='resume'),
    path('cripto/', views.cripto, name='cripto'),

    # Moedas
    path('my-coins/', views.my_coins, name='my-coins'),
    path('my-coins/exclude-coin/<str:coinname>/', views.exclude_coin, name='exclude-coin'),
    path('my-coins/add-coin/<str:ticker>/<str:trading_pair>/', views.add_coin, name='add-coin'),

    # Perfil (CRUD)
    path('perfil/login/', views.login_view, name='login'),
    path('perfil/register/', views.register_view, name='register'),
    path('perfil/logout/', views.logout_view, name='logout'),
    path('perfil/exclude/', views.exclude_user, name='exclude'),
]