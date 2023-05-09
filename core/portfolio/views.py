from django.shortcuts import render
from .models import Project
from django.views.generic import ListView

class HomeView(ListView):
    model = Project
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = 'Principal'
        return context
    
