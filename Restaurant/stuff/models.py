
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Stuff(models.Model):
    name = models.CharField(max_length=50,verbose_name="نام و نام خانوادگی")
    address = models.CharField(max_length=100,verbose_name="ادرس")
    line_of_activity = models.CharField(max_length=70,verbose_name="حوزه فعالیت")
    approved_by = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="تایید شده توسط")
    work_experience = models.IntegerField(verbose_name="سابقه کاری")
    created_at = models.DateTimeField(auto_now=False,auto_now_add=True)
    image =  models.ImageField(upload_to='Stuff_pics',verbose_name="عکس")

    def __str__(self):
        return self.name
    
