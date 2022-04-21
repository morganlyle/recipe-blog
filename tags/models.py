from django.db import models


# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=125)
    author = models.CharField(max_length=100)
    description = models.TextField()
    image = models.URLField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def _str_(self):
        return self.name + " by " + self.author


class Measure(models.Model):
    name = models.CharField(max_length=30, unique=True)
    abbreviation = models.CharField(max_length=10, unique=True)


class FoodItem(models.Model):
    name = models.CharField(max_length=100)

    def _str_(self):
        return (
            str(self.recipe)
            + " "
            + str(self.measure)
            + " "
            + str(self.fooditem)
        )


class Ingredient(models.Model):
    amount = models.FloatField

    recipe = models.ForeignKey(
        Recipe,
        related_name="Ingredients",
        on_delete=models.PROTECT,  # or models.PROTECT
    )

    recipe = models.ForeignKey(
        Recipe, related_name="ingredients", on_delete=models.CASCADE
    )
    measurement = models.ForeignKey(Measure, on_delete=models.PROTECT)
    food = models.ForeignKey(
        FoodItem, related_name="foods", on_delete=models.CASCADE
    )

    def _str_(self):
        return self.name


class Step(models.Model):

    recipe = models.ForeignKey(
        "Step", related_name="steps", on_delete=models.CASCADE
    )

    order = models.PositiveSmallIntegerField

    directions = models.CharField(max_length=300)

    def _str_(self):
        return self.name
