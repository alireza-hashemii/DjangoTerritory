from django.urls import path
from .views import *
app_name = 'about'

urlpatterns = [
    path('',load,name='load')
]