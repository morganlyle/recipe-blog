from django.db import models
from django.conf import settings

USER_MODEL = settings.AUTH_USER_MODEL

# Create your models here.


class MealPlan(models.Model):
    name = models.CharField(max_length=120)
    date = models.DateField(auto_now_add=False)
    owner = models.ForeignKey(
        USER_MODEL,
        related_name=("meal_plan"),
        on_delete=models.CASCADE,
        null=True,
    )

    recipes = models.ManyToManyField("recipes.Recipe", related_name="recipes")

    def __str__(self):
        return str(self.name) + "by: " + str(self.owner)
