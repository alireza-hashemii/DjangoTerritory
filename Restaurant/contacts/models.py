from django.db import models
from django.utils import timezone
# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=50,verbose_name="نام")
    email = models.EmailField(max_length=150,verbose_name="نشانی الکترونیکی")
    person = models.IntegerField(verbose_name="نفرات")
    message = models.TextField(verbose_name="متن پیام")
    created_at = models.DateTimeField(auto_now=False,auto_now_add=True)

    def __str__(self):
        return self.email