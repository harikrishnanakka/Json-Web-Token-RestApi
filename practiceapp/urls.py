from django.contrib import admin
from django.urls import path
from .views import RegisterUser, StudentView


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('register/',RegisterUser.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('basic/',StudentView.as_view()),
    path('basic/<int:id>/',StudentView.as_view())
    
]
 