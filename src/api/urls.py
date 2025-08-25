from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from . import views

app_name = 'api'

urlpatterns = [
    path('tocken/obtain/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('tocken/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('get/dolar/days/<int:days>/', views.get_dolar_for_days, name='get_dolar_for_days'),
    path('get/bitcoin/days/<int:days>/', views.get_bitcoin_for_days, name='get_bitcoin_for_days'),
    path('get/ipca/months/<int:months>/', views.get_ipca_for_months, name='get_ipca_for_days'),
    path('get/inpc/months/<int:months>/', views.get_inpc_for_months, name='get_inpc_for_days'),
    path('get/selic/months/<int:months>/', views.get_selic_for_months, name='get_selic_for_days'),
]
