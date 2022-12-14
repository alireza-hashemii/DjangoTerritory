from django.contrib import admin
from .models import *
# Register your models here.
class BlogAdmin(admin.ModelAdmin):
        list_display = ('title','created_at','related_user')
        list_filter = ('related_user',)
        search_fields = ('title',)
        ordering = ('-title',)
      



admin.site.register(Blog,BlogAdmin)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Comment)


