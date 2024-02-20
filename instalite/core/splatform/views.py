from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Profile, Post , Like , FollowesCount
from django.contrib import auth
from . models import Post ,Comment
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
# Create your views here.

@login_required(login_url="splatform:signin")
def home(request):

    posts = Post.objects.all()
    return render(request,"index.html",{'posts':posts})

    user  = User.objects.get(username = request.user.username)
    user_profile = Profile.objects.get(username=user)
    posts = Post.objects.all()
    return render(request,"index.html",{"user_profile":user_profile,"posts":posts})



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
                auth.login(request,user)
                return redirect("splatform:setting")
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
        

@login_required(login_url="splatform:signin")
def logout(request):
    auth.logout(request)
    return redirect("splatform:signin")


@login_required(login_url="splatform:signin")
def setting(request):
    user_profile = Profile.objects.get(username=request.user)
    if request.method == "POST":
        if request.FILES.get("image") == None:
            user_profile.location = request.POST["location"]
            user_profile.biography = request.POST["bio"]
            user_profile.save()

        elif request.FILES.get("image") != None:
            user_profile.profile_img = request.FILES.get('image')
            user_profile.biography = request.POST["bio"]
            user_profile.location = request.POST["location"]
            user_profile.save()

    return render(request,"setting.html",{"profile":user_profile})



def upload(request):
    if request.method == 'POST':
        user = request.user.username
        image = request.FILES.get('image')
        caption = request.POST['caption']
        new_post = Post.objects.create(user=user,image=image,caption=caption)
        new_post.save()
        return redirect('/')
    else:
        return redirect('/')
    

@login_required(login_url="splatform:signin")
def profile(request,username):
    profile_visitor = request.user.username
    user_object = User.objects.get(username=username)
    user_profile = Profile.objects.get(username=user_object)
    user_posts = Post.objects.filter(user=username)
    context = {
        'profile_visitor':profile_visitor,
        'user_object':user_object,
        'user_profile':user_profile,
        'user_posts':user_posts,
        'lenposts':len(user_posts)
    }
    return render(request,'profile.html',context)

def like_post(request,postid):
    post = Post.objects.get(id = postid)
    is_liked = Like.objects.filter(post_id= post.id, username= post.user)

    if is_liked.exists():
        is_liked.delete()
        post.no_likes -= 1
        post.save()    
        return redirect('/')
    
    elif not is_liked.exists():
        new_like = Like.objects.create(post_id= postid, username= request.user.username)
        new_like.save()
        post.no_likes += 1
        post.save()
        return redirect('/')


@login_required(login_url="splatform:signin")
def follow(request):
    if request.method == 'POST':   
        user = request.POST['user']
        follower = request.POST['follower']

        user_obj = User.objects.get(username=user)
        user_profile = Profile.objects.get(username=user_obj)
        if FollowesCount.objects.filter(follower=follower,user=user).exists():
            delete_follower = FollowesCount.objects.get(follower=follower,user=user)
            delete_follower.delete()
            user_profile.follower -= 1
            return redirect('/profile/' + user)
        else:
            new_follower = FollowesCount.objects.create(follower=follower,user=user)
            new_follower.save()
            user_profile.follower += 1
            return redirect('/profile/' + user)
    else:
        return redirect('/')
    

# def comment(request):
#     if request.method == "POST":
#         post_id = request.POST['post_id']
#         comment = request.POST["comment"]
#         user = request.POST["user"]

#         new_comment = Comment.objects.create(user=user,content=comment)
#         new_comment.save()

#         post = Post.objects.get(id = post_id)
        
#         post.no_comments = post.no_comments + 1
#         post.comments.set([new_comment])
#         post.save()
#         return redirect("/")

#     else:
#         return redirect("/")
