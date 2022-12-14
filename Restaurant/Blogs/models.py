
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=40,verbose_name="عنوان مقاله")
    description = models.CharField(max_length=50,verbose_name="توضیحات")
    content = RichTextField(verbose_name="محتوا")
    created_at = models.DateTimeField(auto_now=False,auto_now_add=True)
    related_user = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'images/')
    category = models.ForeignKey("Category",on_delete=models.CASCADE,verbose_name="دسته بندی مقالات",related_name="blogs")
    tags = models.ManyToManyField("Tag",related_name="blogs",verbose_name="تگ ها",blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"


class Category(models.Model):
    title = models.CharField(max_length=40,verbose_name="عنوان دسته بندی")
    slug = models.SlugField(verbose_name="نام اصلی")
    status = models.BooleanField(verbose_name="نشان داده بشود؟")
    published_at = models.DateField(auto_now=False , auto_now_add=True)

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی  ها"

    def __str__(self):
        return self.title
    

class Tag(models.Model):
    title = models.CharField(max_length=30)
    slug = models.SlugField(verbose_name="نام اصلی")
    published_at = models.DateTimeField(auto_now=False,auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True,auto_now_add=False)

    class Meta:
        verbose_name = "تگ"
        verbose_name_plural = "تگ ها"

    def __str__(self):
        return self.title


class Comment(models.Model):
    blog = models.ForeignKey("Blog",verbose_name="مقاله مربوطه",on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=50,verbose_name="نام و نام خانوادگی")
    email = models.EmailField(max_length=50,verbose_name="نشانی  الکترونیکی")
    message = models.TextField(verbose_name="متن پیام")
    date = models.DateField(auto_now=False,auto_now_add=True,verbose_name="تاریخ")

    def __str__(self):
        return self.email


    