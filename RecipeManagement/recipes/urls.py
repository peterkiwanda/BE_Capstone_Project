# RecipeManagement/urls.py

from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from recipes.views import RecipeViewSet, CategoryViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('recipes.urls')),  # Include the recipes app urls
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
