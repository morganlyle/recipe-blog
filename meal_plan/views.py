from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from recipes.forms import RatingForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class MealPlanListView(ListView):
    model = MealPlan
    template_name = "meal_plan/list.html"
    
    def get_queryset(self):
        return MealPlan.objects.filter(owner=self.request.user)

class MealPlanCreateView(CreateView):
    model = MealPlan
    template_name = "meal_plan/create.html"
    fields = ["name", "description", "image"]
    success_url = reverse_lazy("recipes_list")
    
class MealPlanDetailsView(ListView):