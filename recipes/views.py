from django.db import IntegrityError
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from recipes.forms import RatingForm
from django.contrib.auth.mixins import LoginRequiredMixin

# from django.views.decorators.http import require_http_methods

# try:
# from recipes.forms import RecipeForm
from recipes.models import Ingredient, Recipe, ShoppingItem

# except Exception:
#     RecipeForm = None
#     Recipe = None


def log_rating(request, recipe_id):
    try:
        if request.method == "POST":
            form = RatingForm(request.POST)

            if form.is_valid():
                rating = form.save(commit=False)
                rating.recipe = Recipe.objects.get(pk=recipe_id)
                rating.save()
    except Recipe.DoesNotExist:
        return redirect("recipes_list")

    return redirect("recipe_detail", pk=recipe_id)


class RecipeListView(ListView):
    model = Recipe
    template_name = "recipes/list.html"
    paginate_by = 2


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = "recipes/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["rating_form"] = RatingForm()

        foods = []

        for item in self.request.user.shopping_items.all():

            foods.append(item.food_item)

        context["food_in_shopping_list"] = foods

        return context


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    template_name = "recipes/new.html"
    fields = ["name", "description", "image"]
    success_url = reverse_lazy("recipes_list")


class RecipeUpdateView(LoginRequiredMixin, UpdateView):
    model = Recipe
    template_name = "recipes/edit.html"
    fields = ["name", "author", "description", "image"]
    success_url = reverse_lazy("recipes_list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class RecipeDeleteView(LoginRequiredMixin, DeleteView):
    model = Recipe
    template_name = "recipes/delete.html"
    success_url = reverse_lazy("recipes_list")


class ShoppingItemsListView(LoginRequiredMixin, ListView):
    model = ShoppingItem
    template_name = "shopping_items/list.html"
    success_url = reverse_lazy("shopping_item_list")

    def get_queryset(self):
        return ShoppingItem.objects.filter(user=self.request.user)


def create_shopping_item(request):

    ingredient_id = request.POST.get("ingredient_id")

    ingredient = Ingredient.objects.get(id=ingredient_id)

    user = request.user

    try:

        ShoppingItem.objects.create(
            food_item=ingredient.food,
            user=user,
        )
    except IntegrityError:

        pass
    return redirect("recipe_detail", pk=ingredient.recipe.id)


def delete_all_shopping_items(request):
    ShoppingItem.objects.filter(user=request.user).delete()
    return redirect("shopping_items_list")
