from django.contrib import admin
from .models import (
    Dish,
    Ingredient,
    DishIngredient,
    DietaryRegime,
    MealMoment,
    Occasion,
    Cuisine,
    Color,
    Utensil,
    Season,
)

class DishIngredientInline(admin.TabularInline):
    model = DishIngredient
    extra = 1


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    inlines = [DishIngredientInline]
    
admin.site.register(Ingredient)
admin.site.register(DishIngredient)
admin.site.register(DietaryRegime)
admin.site.register(MealMoment)
admin.site.register(Occasion)
admin.site.register(Cuisine)
admin.site.register(Color)
admin.site.register(Utensil)
admin.site.register(Season)
