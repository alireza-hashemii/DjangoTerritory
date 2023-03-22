from django.shortcuts import render
from .models import Item
from django.views.generic import *
# Create your views here.


def item_list(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, 'home_page.html', context)


class HomeView(ListView):
    model = Item
    template_name = 'home_page.html'


class ItemDetailView(DeleteView):
    model = Item
    template_name = 'product_page.html'
