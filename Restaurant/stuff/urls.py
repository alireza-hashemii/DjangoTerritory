from django.urls import path
from .views import *
app_name = 'stuff'

urlpatterns = [
path('',loading,name='loading')
]