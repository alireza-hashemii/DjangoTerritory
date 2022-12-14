from django.contrib import admin
from .models import Stuff
# Register your models here.

class StuffAdmin(admin.ModelAdmin):
    list_display = ('name','approved_by','created_at')
    ordering = ('created_at',)

admin.site.register(Stuff,StuffAdmin)
