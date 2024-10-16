from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RecipeViewSet

router = DefaultRouter()
router.register(r'', RecipeViewSet)  # Registers the viewset

urlpatterns = [
    path('', include(router.urls)),
]
