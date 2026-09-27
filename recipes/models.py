from django.db import models
from dishes.models import Dish

class Recipe(models.Model):
    dish = models.ForeignKey(
        Dish,
        on_delete=models.CASCADE,
        related_name="recipes",
    )

    language = models.CharField(max_length=10)

    title = models.CharField(max_length=125)

    content = models.TextField()

    def __str__(self):
        return self.title

    