from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path('',PostsView.as_view(),name='posts'),
    path('<int:pk>',PostDetailView.as_view(),name='post_detail')
]
