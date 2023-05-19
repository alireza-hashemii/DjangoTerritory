from django.urls import path
from . import views

app_name = "splatform"
urlpatterns = [
    path("",views.home,name="home"),
    path("signup/",views.signup,name="signup")
]