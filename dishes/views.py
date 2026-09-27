from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from .models import Dish
from .serializers import DishSerializer


class DishViewSet(viewsets.ModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer

    filter_backends = [DjangoFilterBackend]

    filterset_fields = [
        "complexity",
        "cooking",
        "dish_type",
        "cuisine",
        "seasons",
        "meal_moments",
        "occasions",
        "colors",
        "dietary_regimes"
    ]
