from django.contrib import admin
from blog.models import Blog , Category
# Register your models here.

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title','slug','jpublish','category_to_str']
    list_filter = ['status']
    prepopulated_fields = {'slug':('title',)}

    def category_to_str(self,obj):
        categories = " , ".join([category.title for category in obj.category_pubished()])
        if not categories:
            return "-----"
        return categories
    category_to_str.short_description = "دسته بندی ها"
    

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title','jpublish','is_active']        


admin.site.register(Category,CategoryAdmin)