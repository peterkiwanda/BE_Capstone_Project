# recipes/serializers.py

from rest_framework import serializers
from .models import Recipe, Category

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'  # Or specify the fields you want

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
