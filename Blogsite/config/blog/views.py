from django.shortcuts import render
from blog.models import Blog
# Create your views here.

def home(request):
    blogs = Blog.objects.all()
    context = {
        'blogs':blogs,
    }
    return render(request,'index.html',context)


def detail(request,pk):
    blog = Blog.objects.get(pk=pk)
    context = {
        'blog':blog
    }
    return render(request,'post.html',context)