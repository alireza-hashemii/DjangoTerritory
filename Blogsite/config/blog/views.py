from django.shortcuts import render
from django.core.paginator import Paginator
from blog.models import Blog , Category
from django.contrib.auth.models import User
# Create your views here.

def home(request,page=1):
    blog_list = Blog.objects.published()
    paginator = Paginator(blog_list, 3)  
    blogs = paginator.get_page(page)
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


def category(request,slug,page=1):
    category = Category.objects.get(slug=slug,is_active=True)
    blogs_list = category.blogs.published()
    paginator = Paginator(blogs_list, 3)  
    blogs = paginator.get_page(page)
    context = {
        'category': category,
        'blogs':blogs
    }
    return render(request,'category.html',context)


def author_list(request,username):
    author = User.objects.get(username=username)
    blogs = author.blogs.all()
    context = {
        'blogs':blogs
    }
    return render(request,'author_blogs.html',context)

