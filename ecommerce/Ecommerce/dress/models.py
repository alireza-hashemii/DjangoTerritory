from django.db import models
from django.utils import timezone

# Create your models here.
class Dress(models.Model):
    GENDER = (
        ('m',"Men"),
        ('w',"Woman")
    )
    description = models.TextField()
    image = models.ImageField()
    slug = models.SlugField()
    price = models.IntegerField()
    discount = models.IntegerField(blank=True,null=True)
    published = models.DateTimeField(default=timezone.now())
    dressGender = models.CharField(max_length=1,choices=GENDER)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.slug)
