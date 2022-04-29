from django.urls import path
from django.contrib.auth import views as auth_views

from recipes.views import (
    RecipeCreateView,
    RecipeUpdateView,
    log_rating,
    RecipeDetailView,
    RecipeListView,
    RecipeDeleteView,
    ShoppingItemsListView,
    delete_all_shopping_items,
    create_shopping_item,
)

urlpatterns = [
    path("", RecipeListView.as_view(), name="recipes_list"),
    path("<int:pk>/", RecipeDetailView.as_view(), name="recipe_detail"),
    path("new/", RecipeCreateView.as_view(), name="recipe_new"),
    path("<int:pk>/edit/", RecipeUpdateView.as_view(), name="recipe_edit"),
    path("<int:pk>/delete/", RecipeDeleteView.as_view(), name="recipe_delete"),
    path("<int:recipe_id>/ratings/", log_rating, name="recipe_rating"),
    path("accounts/login/", auth_views.LoginView.as_view(), name="login"),
    path(
        "shopping_items/create/",
        create_shopping_item,
        name="shopping_item_create",
    ),
    path(
        "shopping_items/",
        ShoppingItemsListView.as_view(),
        name="shopping_items_list",
    ),
    path(
        "shopping_items/delete,",
        delete_all_shopping_items,
        name="delete_all_shopping_items",
    ),
]
