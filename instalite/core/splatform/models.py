from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    user_id = models.IntegerField()
    biography = models.TextField(blank=True)
    profile_img = models.ImageField(upload_to = 'profile_images',default = 'blank pic.png')
    location = models.CharField(max_length=100,blank=True)
    follower = models.IntegerField(default=0)
    following = models.IntegerField(default=0)

    def __str__(self):
        return self.username.username