class Tag(models.Model):
    name = models.CharField(max_length=20)
    recipes = models.ManyToManyField("recipes.Recipe", related_name="tags")

    def __str__(self):
        return self.name
