from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

app_name = 'api'

urlpatterns = [
    path('tocken/obtain/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('tocken/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
