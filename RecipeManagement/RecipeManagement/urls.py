from django.urls import path, include
from rest_framework.routers import DefaultRouter
from recipes.views import RecipeViewSet
from users.views import UserViewSet
from django.http import HttpResponse  # Import HttpResponse for a simple view

# Create a simple home view for the root URL
def home(request):
    return HttpResponse("<h1>Welcome to the Recipe Management API</h1>")

# Set up the router
router = DefaultRouter()
router.register(r'recipes', RecipeViewSet)
router.register(r'users', UserViewSet)

# Define the URL patterns
urlpatterns = [
    path('', home, name='home'),  # Add this line for the root URL
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),  # for login/logout
]

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns += [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
