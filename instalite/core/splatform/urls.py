from django.urls import path
from . import views

app_name = "splatform"
urlpatterns = [
    path("",views.home,name="home"),
    path("signup/",views.signup,name="signup"),
    path("signin/",views.signin,name="signin"),
    path("upload/",views.upload,name="upload"),
    path("logout/",views.logout,name="logout"),
    path("setting/",views.setting,name="setting")
]