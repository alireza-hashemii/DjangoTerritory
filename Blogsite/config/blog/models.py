from django.db import models
from django.utils import timezone
# Create your models here.

class Blog(models.Model):
    STATUS_CHOICES = (
        ('d', 'پیش‌نویس'),		 # draft
        ('p', "منتشر شده"),		 # publish
    )
    title = models.CharField(max_length=200, verbose_name="عنوان مقاله")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="آدرس مقاله")
    description = models.TextField(verbose_name="محتوا")
    thumbnail = models.ImageField(upload_to="images", verbose_name="تصویر مقاله")
    publish = models.DateTimeField(default=timezone.now, verbose_name="زمان انتشار")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, verbose_name="وضعیت")

    def __str__(self) -> str:
        return self.title