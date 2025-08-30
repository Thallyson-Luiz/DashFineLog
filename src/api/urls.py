from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from . import views

app_name = 'api' # Nome do app

urlpatterns = [
    path('tocken/obtain/', TokenObtainPairView.as_view(), name='token_obtain_pair'), # para obter o token
    path('tocken/refresh/', TokenRefreshView.as_view(), name='token_refresh'), # para atualizar o token
    path('get/dolar/days/<int:days>/', views.get_dolar_for_days, name='get_dolar_for_days'), # para obter as cotações do dolar
    path('get/bitcoin/days/<int:days>/', views.get_bitcoin_for_days, name='get_bitcoin_for_days'), # para obter as cotações do bitcoin
    path('get/ipca/months/<int:months>/', views.get_ipca_for_months, name='get_ipca_for_days'), # para obter as cotações do ipca
    path('get/inpc/months/<int:months>/', views.get_inpc_for_months, name='get_inpc_for_days'), # para obter as cotações do inpc
    path('get/selic/months/<int:months>/', views.get_selic_for_months, name='get_selic_for_days'), # para obter as cotações do selic
]



# Atenção:
#     Caso seja um dev, as views de tocken JWT ainda não foram implementadas em uma funcionabilidade especifica.
#     lembre-se que este Projeto ainda esta em desenvolvimento e a api esta sendo desenvolvida conforme o projeto avança.
#     Obrigado!
