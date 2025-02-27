from django.db.models import Model, CharField, PositiveIntegerField
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Food(Model):
    name = CharField(max_length=100)
    calories = PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(20000)]
    )
