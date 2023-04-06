from django.contrib import admin
from blog.models import Blog , Category
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ['title','slug','publish','category_to_str']
    list_filter = ['status']
    prepopulated_fields = {'slug':('title',)}

    def category_to_str(self,obj):
        categories = " , ".join([category.title for category in obj.category.all()])
        if not categories:
            return "-----"
        return categories
        


admin.site.register(Blog,BlogAdmin)
admin.site.register(Category)