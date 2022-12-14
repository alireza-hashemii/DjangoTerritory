from django.shortcuts import render , get_object_or_404
from .models import Food
# Create your views here.

def list_foods(request):
    list_foods = Food.objects.all()
    context = {
        'Foods':list_foods
    }
    return render(request,'index.html',context)

def detail(request , id):
    food = get_object_or_404(Food,id = id)
    context = {
        'Food':food
    }
    return render(request,'link.html',context)
    