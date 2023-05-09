from django.shortcuts import render,get_object_or_404
from .models import Post

def posts(request):
    posts = Post.objects.all()
    return render(request,'posts.html',{'posts':posts,'titulo':'Posts'})

def post_detail(request, post_id):
    #el get_object_or_404 busca en la base de datos, con el id pasado un objeto/registro, y si no lo encuentra, va a retornar una respuesta 404
    post = get_object_or_404(Post,pk=post_id)
    return render(request,'post_detail.html',{'post':post,'titulo':f'Post {post_id}'})