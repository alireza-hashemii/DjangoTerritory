from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request,"index.html")


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email = email).exists():
                messages.info(request,"Email Taken!")
                return redirect('core:signup')
            elif User.objects.filter(username = username).exists():
                messages.info(request,"Username Taken!")
                return redirect('core:signup')
            else:
                user = User.objects.create(username=username,email=email,password=password)
                user.save()
                user_object = User.objects.get(username = username)
                user_profile = Profile.objects.create(username = user_object , user_id = user_object.id)
                user_profile.save()
                return redirect('core:index')
                
                    
        else:
            messages.info(request,"Passwords are not the same")
            return redirect('core:signup')
            
    else:
        return render(request,'signup.html')