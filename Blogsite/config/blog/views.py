from django.shortcuts import render
from blog.models import Blog , Category
# Create your views here.

def home(request):
    blogs = Blog.objects.all()
    categories = Category.objects.filter(is_active=True)
    context = {
        'blogs':blogs,
        'categories':categories,
    }
    return render(request,'index.html',context)


def detail(request,pk):
    blog = Blog.objects.get(pk=pk)
    context = {
        'blog':blog
    }
    return render(request,'post.html',context)