from django.db import models
from django.conf import settings

class Recipe(models.Model):
    CATEGORY_CHOICES = [
        ('Dessert', 'Dessert'),
        ('Main Course', 'Main Course'),
        ('Appetizer', 'Appetizer'),
        ('Breakfast', 'Breakfast'),
        ('Vegetarian', 'Vegetarian'),
        # Add more categories as needed
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    ingredients = models.TextField(help_text="Enter ingredients separated by commas")
    instructions = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    preparation_time = models.PositiveIntegerField(help_text="Preparation time in minutes")
    cooking_time = models.PositiveIntegerField(help_text="Cooking time in minutes")
    servings = models.PositiveIntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
