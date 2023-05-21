from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Profile
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
# Create your views here.

@login_required(login_url="splatform:signin")
def home(request):
    return render(request,"index.html")


def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        password2 = request.POST["password2"]

        if password == password2 and len(password) >= 8:
            if User.objects.filter(email = email).exists():
                messages.info(request,"Email Taken")
                return redirect("splatform:signup")
            elif User.objects.filter(username=username).exists():
                messages.info(request,"Username Taken")
                return redirect("splatform:signup")
            else:
                user = User.objects.create(username=username,email=email,password=make_password(password))
                user.save()
                user_object = User.objects.get(username=username)
                profile_user = Profile.objects.create(username=user_object,user_id=user_object.id)
                profile_user.save()
                return render(request,"index.html")
        else:
            messages.info(request,"passwords are not the same")
            return redirect("splatform:signup")

    else:
        return render(request,"signup.html")
    

def signin(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,"credentials are invalid")
            return redirect("splatform:signin")
    else:
        return render(request,"signin.html")
        

def logout(request):
    auth.logout(request)
    return redirect("splatform:signin")
