from django.urls import path
from .views import * 
app_name = 'Blogs'

urlpatterns = [
    path('',blog_list,name='blog_list'),
    path('<int:id>/',blog_detail,name='blog_detail'),
    path('tag/<slug:tag>',blog_tag,name='tag'),
    path('category/<slug:category>',blog_category,name='category')
]