from django.shortcuts import render
from.models import *
from .forms import *
# Create your views here.

def contact_list(request):
    contact_form = ContactForm()
    if request.method == "POST":
        contact_form = ContactForm(request.POST)
    if contact_form.is_valid():
        contact_form.save()
    else:
        contact_form = ContactForm()
    
    context = {
        'form':contact_form
    }

    return render(request,'contacts/templates/contact.html',context)
