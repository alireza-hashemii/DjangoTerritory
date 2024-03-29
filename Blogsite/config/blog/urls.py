from django.urls import path
from blog import views

app_name = "blog"

urlpatterns = [
    path('',views.home,name='home'),
    path('page/<int:page>',views.home,name='home'),
    path('<pk>/',views.detail,name='detail'),
    path('category/<slug>',views.category,name='category'),
    path('category/<slug>/page/<int:page>',views.category,name='category'),
    path('author/<str:username>/',views.author_list,name='author-blogs')
]