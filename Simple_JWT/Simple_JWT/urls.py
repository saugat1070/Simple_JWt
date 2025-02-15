
from django.contrib import admin
from django.urls import path
from django.urls import include

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('get_token/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('refresh_token/',TokenRefreshView.as_view(),
         name='refresh'),
    path('verify_token/',TokenVerifyView.as_view(),name='verify_token'),
    path('',include('Token.urls')),
    ]

