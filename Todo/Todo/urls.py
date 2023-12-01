
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_simplejwt.views import TokenVerifyView
from .views import home

from api.views import TodoView , UserSignupView
urlpatterns = [
    path('', home, name="home"),
    path('api/todo/',TodoView.as_view() ),
    path('api/signup/', UserSignupView.as_view() ),
    path('api/todo/delete/', TodoView.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('admin/', admin.site.urls),
    
]
