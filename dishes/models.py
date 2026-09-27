from django.db import models


class DietaryRegime(models.Model):
    code = models.CharField(max_length=20, unique=True)
    label = models.CharField(max_length=125)

    def __str__(self):
        return self.label


class MealMoment(models.Model):
    label = models.CharField(max_length=125)

    def __str__(self):
        return self.label

class Season(models.Model):
    label = models.CharField(max_length=125)

    def __str__(self):
        return self.label
    

class Color(models.Model):
    label = models.CharField(max_length=125)
    hex_value = models.CharField(
        max_length=7,
        blank=True
    )

    def __str__(self):
        return self.label


class Occasion(models.Model):
    label = models.CharField(max_length=125)

    def __str__(self):
        return self.label

class Cuisine(models.Model):
    label = models.CharField(max_length=125)

    def __str__(self):
        return self.label


class Utensil(models.Model):
    label = models.CharField(max_length=125)

    def __str__(self):
        return self.label

# Ingredient
class Ingredient(models.Model):
    name = models.CharField(max_length=125)
    description = models.TextField(blank=True)
    
    class TypeIngredient(models.TextChoices):
        SPICE = 'Spice', 'Epice',
        SAUCE = 'Sauce', 'Sauce',
        VEGETABLE = 'Vegetable', 'Légume',
        CEREAL = 'Cereal', 'Céréal',
        PROTEIN = 'Protein', 'Protéine'

    type_ingredient = models.CharField(
        max_length=25,
        choices=TypeIngredient.choices,
        blank=True
    )
  
    def __str__(self):
        return self.name


# Plat
class Dish(models.Model):
    name = models.CharField(max_length=125)

    def __str__(self):
        return self.name

    dietary_regimes = models.ManyToManyField(
        DietaryRegime,
        blank=True
    )

    seasons = models.ManyToManyField(
        Season,
        blank=True,
    )

    class Complexity(models.TextChoices):
        EASY = "EASY", "Facile"
        MEDIUM = "MEDIUM", "Moyen"
        HARD = "HARD", "Difficile"

    complexity = models.CharField(
        max_length=10,
        choices=Complexity.choices,
    )

    class Cooking(models.TextChoices):
        RAW = "RAW", "Cru"
        COOKED = "COOKED", "Cuit"

    cooking = models.CharField(
        max_length=10,
        choices=Cooking.choices,
    )

    class DishType(models.TextChoices):
        STARTER = "STARTER", "Entrée"
        MAIN = "MAIN", "Plat"
        DESSERT = "DESSERT", "Dessert"

    dish_type = models.CharField(
        max_length=10,
        choices=DishType.choices,
    )

    meal_moments = models.ManyToManyField(
        MealMoment,
        blank=True
    )

    occasions = models.ManyToManyField(
        Occasion,
        blank=True,
    )

    cuisine = models.ForeignKey(
        Cuisine,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="dishes"
    )

    colors = models.ManyToManyField(
        Color,
        blank=True,
    )

    utensils = models.ManyToManyField(
        Utensil,
        blank=True,
    )

    ingredients = models.ManyToManyField(
        Ingredient,
        through="DishIngredient"
    )

# Relation plat-ingredient
class DishIngredient(models.Model):
    dish = models.ForeignKey(
        Dish,
        on_delete=models.CASCADE,
        related_name="dish_ingredients"
    )

    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE
    )

    quantity = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )

    unit = models.CharField(
        max_length=50,
        blank=True
    )

