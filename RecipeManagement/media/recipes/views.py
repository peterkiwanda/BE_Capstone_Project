from rest_framework import viewsets
from .models import Recipe
from .serializers import RecipeSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all().order_by('-created_date')
    serializer_class = RecipeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
