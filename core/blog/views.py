from django.shortcuts import render,get_object_or_404
from .models import Post
from django.views.generic import ListView,DetailView

class PostsView(ListView):
    model = Post
    template_name = 'posts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = 'Posts'
        return context

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = f"Post {kwargs['object'].pk}"
        return context