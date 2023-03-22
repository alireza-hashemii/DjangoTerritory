from django.db import models
from django.utils.translation import gettext as _


# Create your models here.

class Food(models.Model):

    FOOD_TYPE = [
        ('dinner','dinner'),
        ('lunch','lunch'),
        ('drink','drinks')
    ]
    name = models.CharField(_("اسم"),max_length=100)
    description = models.TextField(_("توضیحات"))
    taste = models.CharField(_("طعم"),max_length=100)
    time = models.DateTimeField(_("مدت زمان"))
    pub_date = models.DateField(_("تاریخ انتشار"),auto_now=False,auto_now_add=True)
    price = models.IntegerField(_("قیمت"))
    rate = models.IntegerField(_("امتیاز"),default=0)
    photo = models.ImageField(_("عکس"),upload_to='images/')
    food_type = models.CharField(_("نوع غذا"),max_length=20,default='DRIN',choices=FOOD_TYPE)

    class Meta:
        verbose_name = "غذا"
        verbose_name_plural = "غذاها"


    def __str__(self):
        return self.name




