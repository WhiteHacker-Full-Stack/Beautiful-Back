from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=True)
    surname = models.CharField(max_length=200, blank=True)
    img = models.ImageField(blank=True, upload_to= 'profile/')
    birth_date = models.DateField(blank=True, null=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username

