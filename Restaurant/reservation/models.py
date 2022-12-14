from django.db import models

# Create your models here.
class Reservation(models.Model):
    name = models.CharField(max_length=100,verbose_name="نام")
    email = models.EmailField(max_length=100,verbose_name="ایمیل")
    phone = models.CharField(max_length=100,verbose_name="تلفن")
    number = models.IntegerField(verbose_name="شماره")
    date = models.DateField(auto_now=False,auto_now_add=False,verbose_name="تاریخ")
    time = models.TimeField(auto_now=False,auto_now_add=True,verbose_name="زمان")

    class Meta:
        verbose_name = "رزرو"
        verbose_name_plural = "رزروها"

    def __str__(self):
        return self.name


        