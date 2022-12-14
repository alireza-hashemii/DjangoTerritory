from django.urls import path
from .views import *

app_name = "foods"

urlpatterns = [ 
    path('',list_foods,name='list_foods'),
    path('<int:id>/',detail,name='detail'),

]