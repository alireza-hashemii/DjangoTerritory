from django.contrib import admin
from .models import *
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','created_at')

admin.site.register(Contact,ContactAdmin)