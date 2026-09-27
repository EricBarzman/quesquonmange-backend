from rest_framework import serializers
from .models import (
    Color,
    Cuisine,
    DietaryRegime,
    Dish,
    DishIngredient,
    Ingredient,
    MealMoment,
    Occasion,
    Season,
    Utensil,
)


class DietaryRegimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DietaryRegime
        fields = ["id", "code", "label"]


class MealMomentSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealMoment
        fields = ["id", "label"]


class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields = ["id", "label"]


class OccasionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Occasion
        fields = ["id", "label"]


class CuisineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuisine
        fields = ["id", "label"]


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ["id", "label", "hex_value"]


class UtensilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utensil
        fields = ["id", "label"]


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ["id", "name", "description"]

class DishIngredientSerializer(serializers.ModelSerializer):
    ingredient = IngredientSerializer(read_only=True)

    class Meta:
        model = DishIngredient
        fields = ["ingredient", "quantity", "unit"]


class DishSerializer(serializers.ModelSerializer):
    dietary_regimes = DietaryRegimeSerializer(many=True, read_only=True)
    seasons = SeasonSerializer(many=True, read_only=True)
    meal_moments = MealMomentSerializer(many=True, read_only=True)
    occasions = OccasionSerializer(many=True, read_only=True)

    cuisine = CuisineSerializer(read_only=True)
    colors = ColorSerializer(many=True, read_only=True)
    utensils = UtensilSerializer(many=True, read_only=True)

    ingredients = DishIngredientSerializer(
        source="dish_ingredients",
        many=True,
        read_only=True,
    )

    recipes = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Dish
        fields = [
            "id",
            "name",
            "dietary_regimes",
            "seasons",
            "complexity",
            "cooking",
            "dish_type",
            "meal_moments",
            "occasions",
            "cuisine",
            "colors",
            "utensils",
            "ingredients",
            "recipes",
        ]
