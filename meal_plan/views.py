# from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic.list import ListView

from django.contrib.auth.mixins import LoginRequiredMixin

from meal_plan.models import MealPlan

# Create your views here.


class MealPlanListView(LoginRequiredMixin, ListView):
    model = MealPlan
    template_name = "meal_plan/list.html"

    def get_queryset(self):
        return MealPlan.objects.filter(owner=self.request.user)


class MealPlanCreateView(LoginRequiredMixin, CreateView):
    model = MealPlan
    template_name = "meal_plan/new.html"
    fields = ["name", "date", "owner", "recipes"]
    success_url = reverse_lazy("recipes_list")

    def form_valid(self, form):
        plan = form.save(commit=False)
        plan.owner = self.request.user
        plan.save()
        form.save_m2m()
        return redirect("meal_plan_new")


class MealPlanDetailView(LoginRequiredMixin, DetailView):
    model = MealPlan
    template_name = "meal_plan/details.html"
    success_url = reverse_lazy("meal_plan_list")

    def get_queryset(self):
        return MealPlan.objects.filter(owner=self.request.user)


class MealPlanUpdateView(LoginRequiredMixin, ListView):
    model = MealPlan
    fields = ["names", "owner", "description", "image"]
    template_name = "meal_plan/edit.html"
    success_url = reverse_lazy("meal_plan_list")


class MealPlanDeleteView(LoginRequiredMixin, DeleteView):
    model = MealPlan
    template_name = "meal_plan/delete.html"
    success_url = reverse_lazy("meal_plan_list")

    def get_queryset(self):
        return MealPlan.objects.filter(owner=self.request.user)
