from django.urls import path
from .views import *
app_name = 'reservation'

urlpatterns = [
    path('',view=reserve,name='reserve')
]