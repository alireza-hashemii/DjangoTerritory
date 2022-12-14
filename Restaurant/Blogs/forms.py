from django import forms
from . models import *

class CommentForm(forms.Form):
    name = forms.CharField(max_length=50 ,required=True)
    email = forms.EmailField(max_length=70 , required=True)
    message = forms.CharField(widget=forms.Textarea)