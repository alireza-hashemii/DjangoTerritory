from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Profile
# Create your views here.

def home(request):
    return render(request,"index.html")


def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        password2 = request.POST["password2"]

        if password == password2:
            if User.objects.filter(email = email).exists():
                messages.info(request,"Email Taken")
                return redirect("splatform:signup")
            elif User.objects.filter(username=username).exists():
                messages.info(request,"Username Taken")
                return redirect("splatform:signup")
            else:
                user = User.objects.create(username=username,email=email,password=password)
                user.save()
                user_object = User.objects.get(username=username)
                profile_user = Profile.objects.create(username=user_object,user_id=user_object.id)
                profile_user.save()
                messages.info(request,"Alright")
                return render(request,"index.html")
    else:
        messages.info(request,"Passwords are not the same")
        return render(request,"signup.html")