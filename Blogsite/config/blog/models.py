from django.db import models
from django.utils import timezone
from extensions.utils import jalali_converter
# Create your models here.

class BlogManager(models.Manager):
    def published(self):
        return self.filter(status='p')
    

class Category(models.Model):
    title = models.CharField(max_length=50,verbose_name="عنوان دسته بندی")
    slug = models.SlugField(verbose_name="نشانی دسته بندی")
    position = models.IntegerField(verbose_name="جایگاه دسته بندی")
    is_active = models.BooleanField(verbose_name="دسته بندی فعال باشد ؟")
    publish = models.DateTimeField(auto_now=True,verbose_name="تاریخ")
    class Meta:
        ordering = ['-position']
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"

    def jpublish(self):
        return jalali_converter(self.publish)
    jpublish.short_description = "تاریخ"

    def __str__(self) -> str:
        return self.title


class Blog(models.Model):
    STATUS_CHOICES = (
        ('d', 'پیش‌نویس'),		 # draft
        ('p', "منتشر شده"),		 # publish
    )
    title = models.CharField(max_length=200, verbose_name="عنوان مقاله")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="آدرس مقاله")
    description = models.TextField(verbose_name="محتوا")
    category = models.ManyToManyField(Category,related_name='blogs')
    thumbnail = models.ImageField(upload_to="images", verbose_name="تصویر مقاله")
    publish = models.DateTimeField(default=timezone.now, verbose_name="زمان انتشار")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, verbose_name="وضعیت")

    def __str__(self) -> str:
        return self.title
    
    def jpublish(self):
        return jalali_converter(self.publish)
    jpublish.short_description = "تاریخ"

    def category_pubished(self):
        return self.category.filter(is_active=True)
    
    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"
    
    objects = BlogManager()