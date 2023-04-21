from django.contrib import admin
from blog.models import Blog , Category
# Register your models here.

@admin.action(description="Mark selected stories as published")
def make_published(modeladmin, request, queryset):
    queryset.update(status="p")


@admin.action(description="Mark selected stories as draft")
def make_draft(modeladmin, request, queryset):
    altered_items = queryset.update(status="d")
    if altered_items ==1:
        message_bit = "1 blog was"
    else:
        message_bit = "%s blogs were" %altered_items
    modeladmin.message_user(request,"%s updated succesfuly"%message_bit)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title','image','slug','jpublish','status','category_to_str']
    list_filter = ['status']
    prepopulated_fields = {'slug':('title',)}
    actions = [make_published,make_draft]

    def category_to_str(self,obj):
        categories = " , ".join([category.title for category in obj.category_pubished()])
        if not categories:
            return "-----"
        return categories
    category_to_str.short_description = "دسته بندی ها"
    

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title','jpublish','is_active']        

