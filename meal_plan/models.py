from django.db import models
from django.conf import settings

USER_MODEL = settings.AUTH_USER_MODEL

# Create your models here.


class MealPlan(models.Model):
    name = models.CharField(max_length=120)
    created = models.DateField(auto_now_add=True)
    author = models.ForeignKey(
        USER_MODEL,
        related_name="meal plan",
        on_delete=models.CASCADE,
        null=True,
    )
    recipe = models.ManyToManyField(related_name="recipes")
