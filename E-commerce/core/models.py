from django.conf import settings
from django.db import models
from django.utils import timezone


CATEGORY_CHOICES = (
    ('S', 'Shirt'),
    ('SW', 'Sport-wear'),
    ('OW', 'Out-wear '),

)

LABEL_CHOICES = (
    ('P', 'primary'),
    ('S', 'secondary'),
    ('D', 'danger'),

)


class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.FloatField(null=True, blank=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    label = models.CharField(choices=LABEL_CHOICES, max_length=2)

    def __str__(self):
        return self.title


class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField(timezone.now)
    ordered = models.BooleanField(default=False)
