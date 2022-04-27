from django.urls import path

from meal_plan.views import (
    MealPlanListView,
    MealPlanCreateView,
    MealPlanDetailView,
    MealPlanEditView,
    MealPlanDeleteView,
)

urlpatterns = [
    path("", MealPlanListView.as_view(), name="meal_plan_list"),
    path(
        "meal_plans/create/",
        MealPlanCreateView.as_view(),
        name="meal_plan_create",
    ),
    path(
        "meal_plans/<int:pk>/",
        MealPlanDetailView.as_view(),
        name="meal_plan_detail",
    ),
    path(
        "meal_plans/<int:pk>/edit/",
        MealPlanEditView.as_view(),
        name="meal_plan_edit",
    ),
    path(
        "meal_plans/<int:pk>/delete/",
        MealPlanDeleteView.as_view(),
        name="meal_plan_delete",
    ),
]
