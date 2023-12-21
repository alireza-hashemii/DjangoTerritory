from django.urls import path
from . import views

app_name = "splatform"
urlpatterns = [
    path("",views.home,name="home"),
    path("signup/",views.signup,name="signup"),
    path("signin/",views.signin,name="signin"),
    path("logout/",views.logout,name="logout"),
    path("upload/",views.upload,name="upload"),
    path("follow/",views.follow,name="follow"),
    path("like/<postid>",views.like_post,name="like-post"),
    path("profile/<str:username>",views.profile,name="profile"),
    path("setting/",views.setting,name="setting")
]