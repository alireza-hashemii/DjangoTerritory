from django.shortcuts import render
from .models import Stuff
# Create your views here.

def loading(request):
    list_stuff = Stuff.objects.all()

    context = {
        'list':list_stuff
    } 
    return render (request,'stuff/templates/stuff.html',context)

